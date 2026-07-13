from database.db import db


class Order(db.Model):

    __tablename__ = "orders"

    order_id = db.Column(

        db.Integer,

        primary_key=True

    )

    customer_id = db.Column(

        db.Integer,

        db.ForeignKey(

            "customers.customer_id"

        ),

        nullable=False

    )

    product_id = db.Column(

        db.Integer,

        db.ForeignKey(

            "products.product_id"

        ),

        nullable=False

    )

    quantity = db.Column(

        db.Integer,

        nullable=False

    )

    total_price = db.Column(

        db.Float,

        nullable=False

    )

    def __repr__(self):

        return f"<Order {self.order_id}>"