


from abc import ABC, abstractmethod

class SlotAllocationStrategy(ABC):
    @abstractmethod
    def find_available_slot(self, parking_lot: ParkingLot, vehicle_type: VehicleType) -> ParkingSlot | None:
        pass