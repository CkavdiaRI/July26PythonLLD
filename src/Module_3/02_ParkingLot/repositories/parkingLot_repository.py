
class ParkingLotRepository:
    def __init__(self, parking_lots: dict[int, ParkingLot] | None = None):
        self.parking_lots = parking_lots if parking_lots is not None else {}

    def find_parking_lot_by_id(self, parking_lot_id: int) -> ParkingLot | None:
        return self.parking_lots.get(parking_lot_id)