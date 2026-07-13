from database.db import db


class Customer(db.Model):

    __tablename__ = "customers"

    customer_id = db.Column(

        db.Integer,

        primary_key=True

    )

    name = db.Column(

        db.String(100),

        nullable=False

    )

    phone = db.Column(

        db.String(20),

        nullable=False

    )

    email = db.Column(

        db.String(120),

        unique=True,

        nullable=False

    )

    balance = db.Column(

        db.Float,

        default=0

    )

    orders = db.relationship(

        "Order",

        backref="customer",

        lazy=True,

        cascade="all, delete"

    )

    def __repr__(self):

        return f"<Customer {self.name}>"