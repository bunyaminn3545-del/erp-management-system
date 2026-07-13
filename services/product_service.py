from models.product import Product

from repositories.product_repository import ProductRepository

from services.log_service import LogService


class ProductService:

    def __init__(self):

        self.repository = ProductRepository()

        self.log_service = LogService()

    def get_all_products(self):

        return self.repository.get_all_products()

    def get_product_by_id(

            self,

            product_id):

        return self.repository.get_product_by_id(

            product_id

        )

    def add_product(

            self,

            product_id,

            name,

            price,

            stock):

        if self.repository.product_exists(

                product_id):

            return False, "Product ID already exists."

        product = Product(

            product_id=product_id,

            name=name,

            price=price,

            stock=stock

        )

        self.repository.add_product(

            product

        )

        self.log_service.write_log(

            "admin",

            f"Product {name} added."

        )

        return True, "Product added successfully."

    def update_product(

            self,

            product_id,

            name,

            price,

            stock):

        product = self.repository.get_product_by_id(

            product_id

        )

        if product is None:

            return False, "Product not found."

        product.name = name

        product.price = price

        product.stock = stock

        self.repository.update_product()

        self.log_service.write_log(

            "admin",

            f"Product {product.name} updated."

        )

        return True, "Product updated successfully."

    def delete_product(

            self,

            product_id):

        product = self.repository.get_product_by_id(

            product_id

        )

        if product is None:

            return False, "Product not found."

        product_name = product.name

        self.repository.delete_product(

            product

        )

        self.log_service.write_log(

            "admin",

            f"Product {product_name} deleted."

        )

        return True, "Product deleted successfully."

    def search_product(

            self,

            keyword):

        return self.repository.search_product(

            keyword

        )

    def product_count(self):

        return self.repository.product_count()

    def critical_products(self):

        return self.repository.critical_products()