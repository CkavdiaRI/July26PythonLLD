from dataclasses import dataclass, field

@dataclass # Python shortcut to create classes with init, repr, etc.
class BookMovieRequestDTO:
        user_id: int
        show_id: int
        show_seat_ids: list[int] = field(default_factory=list)