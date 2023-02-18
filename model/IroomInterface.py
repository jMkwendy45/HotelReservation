from model.RoomType import RoomType


class Iroom_interface:

    def __init__(self):
        self._room_number = None
        self._room_price = None
        self._room_type = RoomType
        self._is_free = False

    def set_room_number(self, room_number):
        self._room_number = room_number

    def get_room_number(self):
        return self._room_number

    def set_room_price(self, room_price):
        self._room_price = room_price

    def get_room_price(self):
        return self._room_price

    def set_room_type(self, room_type):
        self._room_type = room_type

    def get_room_type(self):
        return self._room_type

    def set_is_free(self, is_free):
        self._is_free = is_free

    def get_is_free(self):
        return self._is_free

    def __str__(self):
        return f"""
                 Number of rooms: {self._room_number},
                 Price of room: {self._room_price},
                 Type of room: {self._room_type},
                 Free room(s): {self._is_free}
                 """

    def __repr__(self):
        return f"""
                 Number of rooms: {self._room_number},
                 Price of room: {self._room_price},
                 Type of room: {self._room_type},
                 Free room(s): {self._is_free}
                 """
