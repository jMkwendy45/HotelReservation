from abc import ABC, abstractmethod


class IRoomInterFace(ABC):
    @abstractmethod
    def get_room_number(self):
        pass

    @abstractmethod
    def get_price_of_room(self):
        pass

    @abstractmethod
    def get_room_type(self):
        pass

    @abstractmethod
    def is_free(self):
        pass
