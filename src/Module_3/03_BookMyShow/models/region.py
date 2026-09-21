# models/region.py
from models.base_model import BaseModel


class Region(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
