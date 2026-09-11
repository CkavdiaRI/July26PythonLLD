
from models.vehicle import Vehicle

class VehicleRepository:
    _counter: int = 0  # Class-level counter for generating unique IDs

    def __init__(self, vehicles: dict[str, Vehicle] | None = None):
        self.vehicles: dict[str, Vehicle] = vehicles if vehicles is not None else {}

    def find_by_license_plate(self, license_plate: str) -> Vehicle:
        return self.vehicles.get(license_plate)

    def save(self, vehicle: Vehicle) -> None:
        VehicleRepository._counter += 1
        vehicle.id = VehicleRepository._counter  # Assign a unique ID to the vehicle
        self.vehicles[vehicle.license_plate] = vehicle
        return vehicle