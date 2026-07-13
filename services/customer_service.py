from models.customer import Customer

from repositories.customer_repository import CustomerRepository

from services.log_service import LogService


class CustomerService:

    def __init__(self):

        self.repository = CustomerRepository()

        self.log_service = LogService()

    def get_all_customers(self):

        return self.repository.get_all_customers()

    def get_customer_by_id(

            self,

            customer_id):

        return self.repository.get_customer_by_id(

            customer_id

        )

    def add_customer(

            self,

            customer_id,

            name,

            phone,

            email,

            balance):

        if self.repository.customer_exists(

                customer_id):

            return False, "Customer ID already exists."

        customer = Customer(

            customer_id=customer_id,

            name=name,

            phone=phone,

            email=email,

            balance=balance

        )

        self.repository.add_customer(

            customer

        )

        self.log_service.write_log(

            "admin",

            f"Customer {name} created."

        )

        return True, "Customer added successfully."

    def update_customer(

            self,

            customer_id,

            name,

            phone,

            email,

            balance):

        customer = self.repository.get_customer_by_id(

            customer_id

        )

        if customer is None:

            return False, "Customer not found."

        customer.name = name

        customer.phone = phone

        customer.email = email

        customer.balance = balance

        self.repository.update_customer()

        self.log_service.write_log(

            "admin",

            f"Customer {customer.name} updated."

        )

        return True, "Customer updated successfully."

    def delete_customer(

            self,

            customer_id):

        customer = self.repository.get_customer_by_id(

            customer_id

        )

        if customer is None:

            return False, "Customer not found."

        customer_name = customer.name

        self.repository.delete_customer(

            customer

        )

        self.log_service.write_log(

            "admin",

            f"Customer {customer_name} deleted."

        )

        return True, "Customer deleted successfully."

    def search_customer(

            self,

            keyword):

        return self.repository.search_customer(

            keyword

        )

    def customer_count(self):

        return self.repository.customer_count()