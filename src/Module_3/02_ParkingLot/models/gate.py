from __future__ import annotations

from models.base_model import BaseModel
from models.gate_type import GateType
from models.operator import Operator


class Gate(BaseModel):
    def __init__(
        self,
        number: str | None = None,
        type: GateType | None = None,
        current_operator: Operator | None = None,
    ) -> None:
        super().__init__()
        self.number = number
        self.type = type
        self.current_operator = current_operator
