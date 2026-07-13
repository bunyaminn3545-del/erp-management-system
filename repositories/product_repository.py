from database.db import db

from models.product import Product


class ProductRepository:

    def get_all_products(self):

        return Product.query.order_by(

            Product.product_id

        ).all()

    def get_product_by_id(

            self,

            product_id):

        return Product.query.filter_by(

            product_id=product_id

        ).first()

    def add_product(

            self,

            product):

        db.session.add(

            product

        )

        db.session.commit()

    def update_product(self):

        db.session.commit()

    def delete_product(

            self,

            product):

        db.session.delete(

            product

        )

        db.session.commit()

    def product_exists(

            self,

            product_id):

        return self.get_product_by_id(

            product_id

        ) is not None

    def search_product(

            self,

            keyword):

        return Product.query.filter(

            Product.name.ilike(

                f"%{keyword}%"

            )

        ).all()

    def product_count(self):

        return Product.query.count()

    def critical_products(self):

        return Product.query.filter(

            Product.stock <= 5

        ).all()