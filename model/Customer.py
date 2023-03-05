import re


class Customer:
    def __init__(self, first_name, last_name, email, full_name):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._full_name = full_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_last_name(self):
        return self._last_name

    def set_full_name(self, first_name, last_name):
        self._full_name = first_name, last_name

    def get_full_name(self):
        return self._full_name

    def set_email(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            print("Valid Email")
        else:
            print("Invalid Email")
        self._email = email

    def get_email(self):
        return self._email

    def __str__(self):
        return f"""
        First Name {self._first_name}
        Last Name{self._last_name}
        Email{self._email}
        Full Name{self._full_name}
        """
