from dataclasses import dataclass, field

@dataclass # Python shortcut to create classes with init, repr, etc.
class BookMovieResponseDTO:
    booking_id: int
    amount: float
    status: str
    message: str