# models/show_seat.py
from enum import Enum, auto

from models.base_model import BaseModel


class ShowSeatStatus(Enum):
    AVAILABLE = auto()
    UNAVAILABLE = auto()   # theatre-controlled: e.g. a broken seat, switched off for this show
    BOOKED = auto()        # final, paid state
    BLOCKED = auto()       # temporary hold while someone is paying (R10 "seat held during payment")


class ShowSeat(BaseModel):
    def __init__(self, show, seat, show_seat_status, blocked_at=None):
        super().__init__()
        self.show = show
        self.seat = seat
        self.show_seat_status = show_seat_status
        self.blocked_at = blocked_at
