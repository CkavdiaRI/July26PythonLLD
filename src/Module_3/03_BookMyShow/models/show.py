# models/show.py
from models.base_model import BaseModel


class Show(BaseModel):
    def __init__(self, movie, start_time, end_time, screen):
        super().__init__()
        self.movie = movie
        self.start_time = start_time
        self.end_time = end_time
        self.screen = screen
        self.features = []
