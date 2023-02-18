import enum


class RoomType(enum.EnumType):
    SINGLE = "One bed"
    DOUBLE = "Two beds"
    EXECUTIVE = "Lounge inclusive"


    def __str__(self):
        return f"""
                   {self.SINGLE},
                   {self.DOUBLE},
                   {self.EXECUTIVE}
                   """


    def __repr__(self):
        return f"""
                   {self.SINGLE},
                   {self.DOUBLE},
                   {self.EXECUTIVE}
                   """