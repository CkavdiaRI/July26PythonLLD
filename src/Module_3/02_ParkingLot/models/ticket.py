from __future__ import annotations

from datetime import datetime

from models.base_model import BaseModel
from models.gate import Gate
from models.operator import Operator
from models.parking_slot import ParkingSlot
from models.vehicle import Vehicle


class Ticket(BaseModel):
    def __init__(self) -> None:
        super().__init__()
        self.entry_time: datetime | None = None
        self.vehicle: Vehicle | None = None
        self.gate: Gate | None = None
        self.operator: Operator | None = None
        self.parking_slot: ParkingSlot | None = None
