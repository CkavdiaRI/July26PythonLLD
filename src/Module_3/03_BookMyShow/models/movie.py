# models/movie.py
from models.base_model import BaseModel


class Movie(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
