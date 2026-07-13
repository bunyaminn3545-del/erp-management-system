from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session

from services.customer_service import CustomerService


customer_bp = Blueprint(

    "customer",

    __name__

)


customer_service = CustomerService()


@customer_bp.route("/customers")
def customers():

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    keyword = request.args.get(

        "search",

        ""

    ).strip()

    if keyword:

        customer_list = customer_service.search_customer(

            keyword

        )

    else:

        customer_list = customer_service.get_all_customers()

    return render_template(

        "customers/customers.html",

        customers=customer_list,

        keyword=keyword

    )


@customer_bp.route(

    "/customers/add",

    methods=["GET", "POST"]

)
def add_customer():

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    if request.method == "POST":

        success, message = customer_service.add_customer(

            int(request.form["customer_id"]),

            request.form["name"],

            request.form["phone"],

            request.form["email"],

            float(request.form["balance"])

        )

        flash(message)

        if success:

            return redirect(

                url_for("customer.customers")

            )

    return render_template(

        "customers/add_customer.html"

    )


@customer_bp.route(

    "/customers/edit/<int:id>",

    methods=["GET", "POST"]

)
def edit_customer(id):

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    customer = customer_service.get_customer_by_id(

        id

    )

    if customer is None:

        flash("Customer not found.")

        return redirect(

            url_for("customer.customers")

        )

    if request.method == "POST":

        success, message = customer_service.update_customer(

            id,

            request.form["name"],

            request.form["phone"],

            request.form["email"],

            float(request.form["balance"])

        )

        flash(message)

        if success:

            return redirect(

                url_for("customer.customers")

            )

    return render_template(

        "customers/edit_customer.html",

        customer=customer

    )


@customer_bp.route(

    "/customers/delete/<int:id>"

)
def delete_customer(id):

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    success, message = customer_service.delete_customer(

        id

    )

    flash(message)

    return redirect(

        url_for("customer.customers")

    )