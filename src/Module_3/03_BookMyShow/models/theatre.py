# models/theatre.py
from models.base_model import BaseModel


class Theatre(BaseModel):
    def __init__(self, name, region):
        super().__init__()
        self.name = name
        self.region = region
        self.screens = []
