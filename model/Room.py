from abc import ABC

from Data.model.IRoom import IRoomInterFace
from Data.model.RoomType import RoomType
from Data.repositry.RoomInterface import RoomInterface


class Room(IRoomInterFace):
    def __init__(self):
        self._room_number = None
        self._price = None
        self._room_type = RoomType

        if self._room_type == RoomType.SINGLE:
            self._price = 200
        elif self._room_type == RoomType.DOUBLE:
            self._price = 400

    def set_room_number(self, room_number):
        self._room_number = room_number

    def get_room_number(self):
        return self._room_number

    def set_price_of_room(self, room_price):
        self._price = room_price

    def get_price_of_room(self):
        return self._price

    def is_free(self):
        pass

    def get_room_type(self, room_type=None):
        return room_type

    def __str__(self):
        return f"""
        RoomNumber {self._room_number}
        ROOM PRICE{self._price}
        ROOM Type{self._room_type}
        """
