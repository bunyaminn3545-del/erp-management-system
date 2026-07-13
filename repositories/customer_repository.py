from database.db import db

from models.customer import Customer


class CustomerRepository:

    def get_all_customers(self):

        return Customer.query.order_by(

            Customer.customer_id

        ).all()

    def get_customer_by_id(

            self,

            customer_id):

        return Customer.query.filter_by(

            customer_id=customer_id

        ).first()

    def add_customer(

            self,

            customer):

        db.session.add(

            customer

        )

        db.session.commit()

    def update_customer(self):

        db.session.commit()

    def delete_customer(

            self,

            customer):

        db.session.delete(

            customer

        )

        db.session.commit()

    def customer_exists(

            self,

            customer_id):

        customer = self.get_customer_by_id(

            customer_id

        )

        return customer is not None

    def search_customer(

            self,

            keyword):

        return Customer.query.filter(

            Customer.name.ilike(

                f"%{keyword}%"

            )

        ).all()

    def customer_count(self):

        return Customer.query.count()