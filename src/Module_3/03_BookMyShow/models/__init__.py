"""Phase 1: plain classes, exactly as taught in Section 3.

Constructor + plain attributes, nothing database-specific. One class per file,
enums live in the file of the entity they belong to (Feature in screen.py,
ShowSeatStatus in show_seat.py, BookingStatus in booking.py,
PaymentProvider/PaymentStatus in payment.py).

Navigation lists exist only where a requirement needs them:
User.bookings, Theatre.screens, Screen.seats, Show.features, Booking.payments.
Region has no `theatres` list on purpose; Show has no `seats` list on purpose.

Section 5 (the SQLAlchemy mapping pass) happens in the `models` package.
"""
from models.base_model import BaseModel
from models.booking import Booking, BookingStatus
from models.movie import Movie
from models.payment import Payment, PaymentProvider, PaymentStatus
from models.region import Region
from models.screen import Screen, Seat, SeatType
from models.show import Show, ShowSeat, ShowSeatStatus, ShowSeatType
from models.theatre import Theatre
from models.user import User


__all__ = [
    "BaseModel",
    "Booking",
    "BookingStatus",
    "Feature",
    "Movie",
    "Payment",
    "PaymentProvider",
    "PaymentStatus",
    "Region",
    "Screen",
    "Seat",
    "SeatType",
    "Show",
    "ShowSeat",
    "ShowSeatStatus",
    "ShowSeatType",
    "Theatre",
    "User",
]
