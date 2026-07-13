from flask import Flask

from config import Config

from database.db import db

from models.user import User
from models.customer import Customer
from models.product import Product
from models.order import Order
from models.log import Log

from routes.auth_routes import auth_bp
from routes.customer_routes import customer_bp
from routes.product_routes import product_bp
from routes.order_routes import order_bp
from routes.dashboard_routes import dashboard_bp
from routes.export_routes import export_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(product_bp)
app.register_blueprint(order_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(export_bp)

if __name__ == "__main__":
    app.run(debug=True)