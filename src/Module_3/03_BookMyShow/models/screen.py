# models/screen.py
from enum import Enum, auto

from models.base_model import BaseModel


class Feature(Enum):
    THREE_D = auto()
    TWO_D = auto()
    DOLBY = auto()
    HD = auto()
    DOLBY_AUDIO = auto()


class Screen(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.seats = []
        self.features = []
