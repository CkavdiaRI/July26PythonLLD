from __future__ import annotations

from models.base_model import BaseModel
from models.vehicle_type import VehicleType


class Vehicle(BaseModel):
    def __init__(
        self,
        license_plate: str | None = None,
        owner_name: str | None = None,
        vehicle_type: VehicleType | None = None,
    ) -> None:
        super().__init__()
        self.license_plate = license_plate
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type
