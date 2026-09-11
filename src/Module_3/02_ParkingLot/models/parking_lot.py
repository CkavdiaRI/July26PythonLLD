from __future__ import annotations

from models.base_model import BaseModel
from models.gate import Gate
from models.parking_floor import ParkingFloor
from strategy.slot_allocation_strategy import SlotAllocationStrategy


class ParkingLot(BaseModel):
    # status

    # allowed_vehicle_types

    def __init__(
        self,
        name: str | None = None,
        total_capacity: int = 0,
        parking_floors: list[ParkingFloor] | None = None,
        address: str | None = None,
        gates: list[Gate] | None = None,
    ) -> None:
        super().__init__()
        self.name = name
        self.total_capacity = total_capacity
        self.parking_floors = parking_floors if parking_floors is not None else []
        self.address = address
        self.gates = gates if gates is not None else []
        self.slot_allocation_strategy: SlotAllocationStrategy | None = None
