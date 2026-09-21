# models/seat.py
from models.base_model import BaseModel


class Seat(BaseModel):
    def __init__(self, num, seat_type, row_val, col_val):
        super().__init__()
        self.num = num
        self.seat_type = seat_type
        self.row_val = row_val
        self.col_val = col_val
