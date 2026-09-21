# models/show_seat_type.py
from models.base_model import BaseModel


class ShowSeatType(BaseModel):
    def __init__(self, show, seat_type, price):
        super().__init__()
        self.show = show
        self.seat_type = seat_type
        self.price = price
