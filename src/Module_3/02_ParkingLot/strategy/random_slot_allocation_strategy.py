from strategy.slot_allocation_strategy import SlotAllocationStrategy
from models.vehicle import VehicleType
from models.parking_lot import ParkingLot
from models.parking_slot import ParkingSlot
import random



class RandomSlotAllocationStrategy(SlotAllocationStrategy):
    def find_available_slot(self, parking_lot: ParkingLot, vehicle_type: VehicleType) -> ParkingSlot | None:
        # Filter the slots based on the vehicle type and availability
        available_slots = [
            slot for slot in parking_lot.slots
            if slot.slot_type == vehicle_type and slot.is_available
        ]
        
        if not available_slots:
            return None
        
        # Randomly select an available slot
        return random.choice(available_slots)