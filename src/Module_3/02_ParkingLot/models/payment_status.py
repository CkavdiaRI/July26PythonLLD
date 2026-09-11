from enum import Enum, auto


class PaymentStatus(Enum):
    PENDING = auto()
    FAILED = auto()
    SUCCESS = auto()
