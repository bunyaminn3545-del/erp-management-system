from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session

from services.order_service import OrderService
from services.customer_service import CustomerService
from services.product_service import ProductService


order_bp = Blueprint(

    "order",

    __name__

)

order_service = OrderService()

customer_service = CustomerService()

product_service = ProductService()


@order_bp.route("/orders")
def orders():

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    orders = order_service.get_all_orders()

    return render_template(

        "orders/orders.html",

        orders=orders

    )


@order_bp.route(

    "/orders/add",

    methods=["GET", "POST"]

)
def add_order():

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    customers = customer_service.get_all_customers()

    products = product_service.get_all_products()

    if request.method == "POST":

        success, message = order_service.create_order(

            int(request.form["order_id"]),

            int(request.form["customer_id"]),

            int(request.form["product_id"]),

            int(request.form["quantity"])

        )

        flash(message)

        if success:

            return redirect(

                url_for("order.orders")

            )

    return render_template(

        "orders/add_order.html",

        customers=customers,

        products=products

    )


@order_bp.route(

    "/orders/delete/<int:id>"

)
def delete_order(id):

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    success, message = order_service.delete_order(

        id

    )

    flash(message)

    return redirect(

        url_for("order.orders")

    )