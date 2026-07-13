from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session

from services.order_service import OrderService
from services.product_service import ProductService
from services.log_service import LogService


dashboard_bp = Blueprint(

    "dashboard",

    __name__

)

order_service = OrderService()

product_service = ProductService()

log_service = LogService()


@dashboard_bp.route("/dashboard")
def dashboard():

    if "username" not in session:

        return redirect(

            url_for(

                "auth.login"

            )

        )

    dashboard_information = (

        order_service.get_dashboard_information()

    )

    critical_products = (

        product_service.critical_products()

    )

    logs = (

        log_service.get_logs()

    )

    return render_template(

        "dashboard.html",

        dashboard=dashboard_information,

        critical_products=critical_products,

        logs=logs

    )