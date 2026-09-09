
from .parking_slot import ParkingSlot
from .base_model import BaseModel



class ParkingFloor(BaseModel):
    def __init__(
        self,
        number: int | None = None,
        parking_slots: list[ParkingSlot] | None = None,
        ) -> None:
            super().__init__()
            self.number = number
            self.parking_slots = parking_slots if parking_slots is not None else []