from typing import List

from Data.model.Customer import Customer
from Data.model.Reservation import Reservation
from Data.model.Room import Room
from service.customerService import CustomerService
from service.reservationService import ReservationService


class AdminResource:
    def __init__(self, customer_service: CustomerService, reservation_service: ReservationService):
        self.customer_service = customer_service
        self.reservation_service = reservation_service

    def get_customer(self, customer_email: str) -> Customer:
        return self.customer_service.get_customer(customer_email)

    def add_room(self, room: Room) -> str:
        return self.reservation_service.add_room(room)

    def get_all_rooms(self) -> List[Room]:
        return self.reservation_service.get_all_rooms()

    def get_all_customers(self) -> List[Customer]:
        return self.customer_service.get_all_customers()

    def display_all_reservations(self) -> List[Reservation]:
        return self.reservation_service.get_all_reservations()