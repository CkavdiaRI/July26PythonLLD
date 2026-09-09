from .response_status import ResponseStatus

class IssueTicketResponseDto:
    def __init__(self) -> None:
        self.ticket_id: int = 0
        self.floor_number: int = 0
        self.slot_number: int = 0

        self.status: ResponseStatus | None = None
        self.message: str | None = None

