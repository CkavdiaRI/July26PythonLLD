# models/seat_type.py
from models.base_model import BaseModel


class SeatType(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name 
