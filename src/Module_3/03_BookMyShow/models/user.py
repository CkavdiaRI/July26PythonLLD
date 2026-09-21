# models/user.py
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, name, email, password):
        super().__init__()
        self.name = name
        self.email = email
        self.password = password
        self.bookings = []
