from models.order import Order

from repositories.order_repository import OrderRepository
from repositories.customer_repository import CustomerRepository
from repositories.product_repository import ProductRepository

from services.log_service import LogService


class OrderService:

    def __init__(self):

        self.order_repository = OrderRepository()

        self.customer_repository = CustomerRepository()

        self.product_repository = ProductRepository()

        self.log_service = LogService()

    def get_all_orders(self):

        return self.order_repository.get_all_orders()

    def get_order_by_id(

            self,

            order_id):

        return self.order_repository.get_order_by_id(

            order_id

        )

    def create_order(

            self,

            order_id,

            customer_id,

            product_id,

            quantity):

        if self.order_repository.get_order_by_id(

                order_id):

            return False, "Order ID already exists."

        customer = self.customer_repository.get_customer_by_id(

            customer_id

        )

        if customer is None:

            return False, "Customer not found."

        product = self.product_repository.get_product_by_id(

            product_id

        )

        if product is None:

            return False, "Product not found."

        if quantity <= 0:

            return False, "Quantity must be greater than zero."

        if product.stock < quantity:

            return False, "Insufficient stock."

        total_price = quantity * product.price

        order = Order(

            order_id=order_id,

            customer_id=customer.customer_id,

            product_id=product.product_id,

            quantity=quantity,

            total_price=total_price

        )

        product.stock -= quantity

        self.product_repository.update_product()

        self.order_repository.add_order(

            order

        )

        self.log_service.write_log(

            "admin",

            f"Order #{order_id} created."

        )

        return True, "Order created successfully."

    def delete_order(

            self,

            order_id):

        order = self.order_repository.get_order_by_id(

            order_id

        )

        if order is None:

            return False, "Order not found."

        product = self.product_repository.get_product_by_id(

            order.product_id

        )

        if product is not None:

            product.stock += order.quantity

            self.product_repository.update_product()

        self.order_repository.delete_order(

            order

        )

        self.log_service.write_log(

            "admin",

            f"Order #{order_id} deleted."

        )

        return True, "Order deleted successfully."

    def order_count(self):

        return self.order_repository.order_count()

    def total_sales(self):

        return self.order_repository.total_sales()

    def get_dashboard_information(self):

        return {

            "customer_count":

                self.customer_repository.customer_count(),

            "product_count":

                self.product_repository.product_count(),

            "order_count":

                self.order_repository.order_count(),

            "total_sales":

                self.order_repository.total_sales()

        }