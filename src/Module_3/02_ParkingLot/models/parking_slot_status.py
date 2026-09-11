from enum import Enum, auto


class ParkingSlotStatus(Enum):
    EMPTY = auto()
    FILLED = auto()
    UNDER_MAINTENANCE = auto()
