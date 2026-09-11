from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from models.base_model import BaseModel
from models.gate import Gate
from models.operator import Operator
from models.ticket import Ticket

if TYPE_CHECKING:
    from models.payment import Payment


class Bill(BaseModel):
    def __init__(
        self,
        exit_time: datetime | None = None,
        ticket: Ticket | None = None,
        total_amount: int = 0,
        gate: Gate | None = None,
        operator: Operator | None = None,
        payments: list[Payment] | None = None,
    ) -> None:
        super().__init__()
        self.exit_time = exit_time
        self.ticket = ticket
        self.total_amount = total_amount
        self.gate = gate
        self.operator = operator
        self.payments = payments if payments is not None else []
