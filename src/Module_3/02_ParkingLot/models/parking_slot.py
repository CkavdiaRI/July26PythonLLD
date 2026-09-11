from __future__ import annotations

from models.base_model import BaseModel
from models.parking_floor import ParkingFloor
from models.parking_slot_status import ParkingSlotStatus
from models.vehicle_type import VehicleType


class ParkingSlot(BaseModel):
    def __init__(
        self,
        number: str | None = None,
        parking_floor: ParkingFloor | None = None,
        slot_status: ParkingSlotStatus = ParkingSlotStatus.EMPTY,
        allowed_vehicle_type: VehicleType | None = None,
    ) -> None:
        super().__init__()
        self.number = number
        self.parking_floor = parking_floor
        self.slot_status = slot_status
        # only one type of vehicle on every slot
        self.allowed_vehicle_type = allowed_vehicle_type
