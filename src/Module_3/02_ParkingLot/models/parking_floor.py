from __future__ import annotations

from typing import TYPE_CHECKING

from models.base_model import BaseModel

if TYPE_CHECKING:
    from models.parking_slot import ParkingSlot


class ParkingFloor(BaseModel):
    def __init__(
        self,
        number: str | None = None,
        parking_slots: list[ParkingSlot] | None = None,
    ) -> None:
        super().__init__()
        self.number = number
        self.parking_slots = parking_slots if parking_slots is not None else []
