from __future__ import annotations

from models.base_model import BaseModel


class Operator(BaseModel):
    def __init__(self, name: str | None = None) -> None:
        super().__init__()
        self.name = name
