import enum


class roomReservationStatus(enum.Enum):
    AVAILABLE = 1
    RESERVED = 2


class RoomType(enum.EnumType):
    SINGLE = "one Bed -->1"
    DOUBLE = "Two Bed--->2"

    def __str__(self):
        return f"""
        SINGLE
        DOUBLE
        """
