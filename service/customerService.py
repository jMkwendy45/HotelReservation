from Data.model.Customer import Customer


class CustomerService:

    def __init__(self):
        self.customers = {}

    def add_customer(self, email, first_name, last_name, full_name):
        if email in self.customers:
            raise Exception("Customer with email already exists")
        customer = Customer(email, first_name, last_name, full_name)
        self.customers[email] = customer
        return customer

    def get_customer(self, customer_email):
        return self.customers.get(customer_email)

    def get_all_customers(self):
        return self.customers.values()

    def create_customer(self, email, first_name, last_name):
        pass
