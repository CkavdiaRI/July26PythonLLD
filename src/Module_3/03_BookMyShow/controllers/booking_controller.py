# DTOs
# Request DTOs  -> user_id, show_id, show_seat_ids
# Response DTOs -> booking_id, amount, status, message

from models import Booking
from services.booking_service import BookingService
from dtos.book_movie_request_dto import BookMovieRequestDTO
from dtos.book_movie_response_dto import BookMovieResponseDTO
from dtos.response_status import ResponseStatus

class BookingController:
    def __init__(self, booking_service: BookingService):
        self.booking_service = booking_service

    def book_movie(self, request: BookMovieRequestDTO) -> BookMovieResponseDTO:
        response = BookMovieResponseDTO()
        try:
            booking = self.booking_service.book_movie(request.user_id, request.show_id, request.show_seat_ids)
            response.booking_id = booking.id
            response.amount = booking.amount
            response.status = ResponseStatus.SUCCESS.value
            response.message = "Booking successful"
        except Exception as e:
            response.status = ResponseStatus.FAILURE
            response.message = f"Error occurred while booking movie: {e}"
        return response

