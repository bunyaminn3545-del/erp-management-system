from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)
auth_service = AuthService()

@auth_bp.route("/")
def home():
    if "username" in session:
        return redirect(url_for("dashboard.dashboard"))
    return redirect(url_for("auth.login"))

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("dashboard.dashboard"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        success, result = auth_service.login(username, password)

        if success:
            session["username"] = username
            flash("Giriş başarılı.", "success")
            return redirect(url_for("dashboard.dashboard"))
        else:
            flash(str(result), "danger")

    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        success, message = auth_service.register(username, password)

        if success:
            flash(message, "success")
            return redirect(url_for("auth.login"))
        else:
            flash(message, "danger")

    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Çıkış yapıldı.", "success")
    return redirect(url_for("auth.login"))