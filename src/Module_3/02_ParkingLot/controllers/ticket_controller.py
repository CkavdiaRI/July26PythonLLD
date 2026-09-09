from dtos.issue_ticket_request_dto import IssueTicketRequestDTO
from dtos.issue_ticket_response_dto import IssueTicketResponseDTO
from dtos.response_status import ResponseStatus

class TicketController:
    def __init__(self, ticket_service) -> None:
        self.ticket_service = ticket_service

    def issue_ticket(self, request: IssueTicketRequestDTO) -> IssueTicketResponseDTO:
        response = IssueTicketResponseDTO()

        try:
            ticket = self.ticket_service.issue_ticket(
                license_plate=request.license_plate,
                vehicle_type=request.vehicle_type,
                owner_name=request.owner_name,
                gate_id=request.gate_id,
                parking_lot_id=request.parking_lot_id
            )

            response.ticket_id = ticket.id
            response.floor_number = ticket.parking_slot.parking_floor.number
            response.slot_number = ticket.parking_slot.number

            response.status = ResponseStatus.SUCCESS
            response.message = "Ticket issued successfully."


        except Exception as e:
            response.status = ResponseStatus.FAILURE
            response.message = str(e)

        return response
