from models.ticket import Ticket
from models.vehicle import Vehicle
from repositories.gate_repository import GateRepository
from repositories.vehicle_repository import VehicleRepository
from repositories.parkingLot_repository import ParkingLotRepository
from datetime import datetime

class TicketService:
    def __init__(self,
        gate_repository: GateRepository,
        vehicle_repository: VehicleRepository,
        parking_lot_repository: ParkingLotRepository
        ) -> None:
        pass

    def issue_ticket(
        self,
        license_plate: str,
        vehicle_type: str,
        owner_name: str,
        gate_id: int,
        parking_lot_id: int,
        ) -> Ticket:
        # Implement the logic to issue a ticket

        # Talk to the database
        # Get the gate by gate id

        gate = self.gate_repository.get_gate_by_id(gate_id)
        if gate is None:
            raise RuntimeError(f"Gate with ID {gate_id} not found.")

        vehicle = self.vehicle_repository.find_by_license_plate(license_plate)
        if vehicle is None:
            vehicle = Vehicle(license_plate=license_plate, vehicle_type=vehicle_type, owner_name=owner_name)

            # save the vehicle to the database
            self.vehicle_repository.save(vehicle)

        parking_lot = self.parking_lot_repository.find_parking_lot_by_id(parking_lot_id)
        if parking_lot is None:
            raise RuntimeError(f"Parking lot with ID {parking_lot_id} not found.")

        # Call the strategy to find the available slot for the vehicle type
        parking_slot = self.slot_allocation_strategy.find_available_slot(parking_lot, vehicle_type)

        if parking_slot is None:
            raise RuntimeError(f"No available slot for vehicle type {vehicle_type} in parking lot {parking_lot_id}.")

        ticket = Ticket()
        ticket.vehicle = vehicle
        ticket.parking_slot = parking_slot
        ticket.gate = gate
        ticket.entry_time = datetime.now()
        ticket.operator = gate.current_operator

        # Save the ticket to the database
        # TODO

        return ticket







# Client -> Controller via DTO -> Service -> Repository -> Database
