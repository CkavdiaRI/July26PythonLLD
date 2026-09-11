from __future__ import annotations

from datetime import datetime

from models.base_model import BaseModel
from models.bill import Bill
from models.payment_mode import PaymentMode
from models.payment_status import PaymentStatus


class Payment(BaseModel):
    def __init__(
        self,
        date: datetime | None = None,
        total_amount: int = 0,
        status: PaymentStatus | None = None,
        payment_mode: PaymentMode | None = None,
        bill: Bill | None = None,
    ) -> None:
        super().__init__()
        self.date = date
        self.total_amount = total_amount
        self.status = status
        self.payment_mode = payment_mode
        self.bill = bill
