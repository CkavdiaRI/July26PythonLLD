

class IssueTicketRequestDto:
    def __init__(
        self,
        owner_name: str | None = None,
        license_plate: str | None = None,
        vehicle_type: str | None = None,
        gate_id: int = 0,
        parking_lot_id: int = 0,
    ) -> None:
        self.owner_name = owner_name
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.gate_id = gate_id
        self.parking_lot_id = parking_lot_id