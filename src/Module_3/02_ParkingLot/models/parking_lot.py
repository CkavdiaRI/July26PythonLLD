
from models.base_model import BaseModel
from models.parking_floor import ParkingFloor
from models.gate import Gate
from typing import List


class ParkingLot(BaseModel):
    def __init__(
        self,
        name: str | None = None,
        address: str | None = None,
        parking_floors: List[ParkingFloor] | None = None,
        total_capacity: int | None = None,
        gates: List[Gate] | None = None,
        ) -> None:
            super().__init__()
            self.name = name
            self.address = address
            self.parking_floors = parking_floors if parking_floors is not None else []
            self.total_capacity = total_capacity
            self.gates = gates if gates is not None else []