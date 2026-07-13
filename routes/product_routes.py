from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session

from services.product_service import ProductService


product_bp = Blueprint(

    "product",

    __name__

)


product_service = ProductService()


@product_bp.route("/products")
def products():

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    keyword = request.args.get(

        "search",

        ""

    ).strip()

    if keyword:

        product_list = product_service.search_product(

            keyword

        )

    else:

        product_list = product_service.get_all_products()

    return render_template(

        "products/products.html",

        products=product_list,

        keyword=keyword

    )


@product_bp.route(

    "/products/add",

    methods=["GET", "POST"]

)
def add_product():

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    if request.method == "POST":

        success, message = product_service.add_product(

            int(request.form["product_id"]),

            request.form["name"],

            float(request.form["price"]),

            int(request.form["stock"])

        )

        flash(message)

        if success:

            return redirect(

                url_for("product.products")

            )

    return render_template(

        "products/add_product.html"

    )


@product_bp.route(

    "/products/edit/<int:id>",

    methods=["GET", "POST"]

)
def edit_product(id):

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    product = product_service.get_product_by_id(

        id

    )

    if product is None:

        flash(

            "Product not found."

        )

        return redirect(

            url_for("product.products")

        )

    if request.method == "POST":

        success, message = product_service.update_product(

            id,

            request.form["name"],

            float(request.form["price"]),

            int(request.form["stock"])

        )

        flash(message)

        if success:

            return redirect(

                url_for("product.products")

            )

    return render_template(

        "products/edit_product.html",

        product=product

    )


@product_bp.route(

    "/products/delete/<int:id>"

)
def delete_product(id):

    if "username" not in session:

        return redirect(

            url_for("auth.login")

        )

    success, message = product_service.delete_product(

        id

    )

    flash(message)

    return redirect(

        url_for("product.products")

    )