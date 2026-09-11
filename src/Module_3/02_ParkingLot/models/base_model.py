from __future__ import annotations

from datetime import datetime


class BaseModel:
    def __init__(self) -> None:
        self.id: int = 0
        self.created_at: datetime | None = None
        self.updated_at: datetime | None = None
