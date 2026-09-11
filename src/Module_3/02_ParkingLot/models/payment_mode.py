from enum import Enum, auto


class PaymentMode(Enum):
    CASH = auto()
    CC = auto()
    DC = auto()
    UPI = auto()
