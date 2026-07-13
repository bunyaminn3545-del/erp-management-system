from database.db import db


class Product(db.Model):

    __tablename__ = "products"

    product_id = db.Column(

        db.Integer,

        primary_key=True

    )

    name = db.Column(

        db.String(100),

        nullable=False

    )

    price = db.Column(

        db.Float,

        nullable=False

    )

    stock = db.Column(

        db.Integer,

        default=0

    )

    orders = db.relationship(

        "Order",

        backref="product",

        lazy=True,

        cascade="all, delete"

    )

    def __repr__(self):

        return f"<Product {self.name}>"