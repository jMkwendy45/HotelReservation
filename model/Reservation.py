import datetime

from Data.model.Customer import Customer
from Data.model.Room import Room


class Reservation:

    def __init__(self, customer, date_check_in, date_check_out, room):
        self._customer = customer
        self._Date_check_in_date = date_check_in
        self._Date_check_out_date = date_check_out
        self._IRoom = room

    def __str__(self):
        return f"""
        Customer {self._customer}
        Check in date{self._Date_check_in_date}
        Check out date{self._Date_check_out_date}
        """
