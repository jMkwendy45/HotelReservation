from Data.model.Customer import Customer
from Data.model.Reservation import Reservation
from Data.model.Room import Room


class ReservationService:
    def __init__(self):
        self.rooms = {}
        self.reservations = []

    def add_room(self, room):
        self.rooms[room.get_room_number()] = room

    def get_room(self, room_id):
        return self.rooms.get(room_id)

    def reserve_a_room(self, customer, room, check_in_date, check_out_date):
        if not room.is_free(check_in_date, check_out_date):
            raise Exception("Room is already reserved for selected dates")

        reservation = Reservation(customer, room, check_in_date, check_out_date)
        self.reservations.append(reservation)
        room.reserve(check_in_date, check_out_date)
        return reservation

    def find_rooms(self, check_in_date, check_out_date):
        available_rooms = []
        for room in self.rooms.values():
            if room.is_free(check_in_date, check_out_date):
                available_rooms.append(room)
        return available_rooms

    def get_customers_reservations(self, customer):
        return [r for r in self.reservations if r.customer == customer]

    def print_reservations(self):
        for reservation in self.reservations:
            print(reservation)

    def get_all_reservations(self):
        pass

    def get_all_rooms(self):
        pass

