from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from models import Booking, BookingStatus
from models.show_seat import ShowSeatStatus
from repositories import ShowRepo, UserRepo, ShowSeatRepo

class BookingService:

    MAX_SEATS_PER_BOOKING = 10
    EXPIRY_MINUTES = 15

#    def __init__(self, session) #
    def __init__(self, engine, price_calulcator):
        self.engine = engine,
        self,price_calulcator = price_calulcator


    def book_movie(self, user_id: int, show_id: int, seat_ids: list[int]) -> Booking:
        # handle seat cap requirement
        if(len(seat_ids) > self.MAX_SEATS_PER_BOOKING):
            raise ValueError()

        connection = self.engine.connect().execute_options(
            isolation_level = "SERIALIZABLE"
        )
        session = Session(bind = connection, expiry_on_commit = False)

        try:
            user_repository = UserRepo(session)
            show_repository = ShowRepo(session)
            show_seat_repository = ShowSeatRepo(session)

            user = user_repository.find_by_id(user_id)
            if user is None :
                raise ValueError()

            show = show_repository.find_by_id(show_id)
            if show is None :
                raise ValueError()

            show_seats = show_seat_repository.find_all_by_id(seat_ids)

            # Lazily update the BLOCKED Seat status
            for show_seat in show_seats:
                is_available = show_seat.show_seat_status is ShowSeatStatus.AVAILABLE

                is_expired_block = (
                    show_seat.show_seat_status is ShowSeatStatus.BLOCKED
                    and show_seat.blocked_at is not None
                    and datetime.now() - show_seat.blocked_at
                    > timedelta(minutes=self.EXPIRY_MINUTES)
                )

                if not (is_available or is_expired_block):
                    raise RuntimeError(
                        f"ShowSeat is not available: {show_seat.id}"
                    )

            # Use soft lock and also update the database
            for show_seat in show_seats:
                show_seat.show_seat_status = ShowSeatStatus.BLOCKED
                show_seat.blocked_at = datetime.now()

            # Caculate the price using the price calculator service
            amount = 100

            # Then finally create booking object with payment in PENDING status
            booking = Booking(
                user=user,
                show=show,
                show_seats=show_seats,
                amount=amount,
                booking_status=BookingStatus.PENDING,
                booked_at=datetime.now()
            )
            session.add(booking)

            # Commit everyting together
            session.commit()
            return booking

        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
            connection.close()



# 1. User should not be able to book more than 10 seats in a single booking.
# 2. Fetch user & show objects from the database using user_id and show_id.
# 3. fetch show seats from the database using show_seat_ids.
# 4. Check if the show seats are available for booking.
# 5. Handling concurrency issues when multiple users try to book the same seat simultaneously.
# 6. Calculate the total amount for the booking based on the number of seats and their prices.
# 7. Create booking with pending payment
# 8. Save the booking to the database.
# 9. Handle exceptions
