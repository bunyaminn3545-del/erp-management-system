from flask import Blueprint
from flask import send_file
from flask import redirect
from flask import url_for
from flask import session

from services.excel_service import ExcelService


export_bp = Blueprint(

    "export",

    __name__

)

excel_service = ExcelService()


@export_bp.route("/export/customers")
def export_customers():

    if "username" not in session:

        return redirect(

            url_for(

                "auth.login"

            )

        )

    excel_service.export_customers()

    return send_file(

        "exports/customers.xlsx",

        as_attachment=True

    )


@export_bp.route("/export/products")
def export_products():

    if "username" not in session:

        return redirect(

            url_for(

                "auth.login"

            )

        )

    excel_service.export_products()

    return send_file(

        "exports/products.xlsx",

        as_attachment=True

    )


@export_bp.route("/export/orders")
def export_orders():

    if "username" not in session:

        return redirect(

            url_for(

                "auth.login"

            )

        )

    excel_service.export_orders()

    return send_file(

        "exports/orders.xlsx",

        as_attachment=True

    )