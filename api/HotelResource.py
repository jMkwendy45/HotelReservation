from datetime import date
from typing import List

from Data.model.Customer import Customer
from Data.model.Reservation import Reservation
from Data.model.Room import Room
from service.customerService import CustomerService
from service.reservationService import ReservationService


class HotelResource:
    def __init__(self, customer_service: CustomerService, reservation_service: ReservationService):
        self.customer_service = customer_service
        self.reservation_service = reservation_service

    def add_customer(self, email: str, first_name: str, last_name: str, full_name: str) -> str:
        return self.customer_service.add_customer(email, first_name, last_name, full_name)

    def create_customer(self, email: str, first_name: str, last_name: str) -> Customer:
        return self.customer_service.create_customer(email, first_name, last_name)

    def get_customer(self, customer_email: str) -> Customer:
        return self.customer_service.get_customer(customer_email)

    def get_all_customers(self) -> List[Customer]:
        return self.customer_service.get_all_customers()

    def get_room(self, room_number: int) -> Room:
        return self.reservation_service.get_room(room_number)

    def book_a_room(self, customer_email: str, room_number: int, check_in_date: date,
                    check_out_date: date) -> Reservation:
        customer = self.customer_service.get_customer(customer_email)
        room = self.reservation_service.get_room(room_number)
        return self.reservation_service.reserve_a_room(customer, room, check_in_date, check_out_date)

    def get_customer_reservations(self, customer_email: str) -> List[Reservation]:
        customer = self.customer_service.get_customer(customer_email)
        return self.reservation_service.get_customers_reservations(customer)

    def find_a_room(self, check_in_date: date, check_out_date: date) -> Room:
        return self.reservation_service.find_rooms(check_in_date, check_out_date)
