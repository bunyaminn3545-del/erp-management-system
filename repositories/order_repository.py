from database.db import db

from models.order import Order


class OrderRepository:

    def get_all_orders(self):

        return Order.query.order_by(

            Order.order_id

        ).all()

    def get_order_by_id(

            self,

            order_id):

        return Order.query.filter_by(

            order_id=order_id

        ).first()

    def add_order(

            self,

            order):

        db.session.add(

            order

        )

        db.session.commit()

    def delete_order(

            self,

            order):

        db.session.delete(

            order

        )

        db.session.commit()

    def order_count(self):

        return Order.query.count()

    def total_sales(self):

        orders = self.get_all_orders()

        total = 0

        for order in orders:

            total += order.total_price

        return total