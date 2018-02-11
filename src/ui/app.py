from flask import Flask, render_template

from src.ui.models.customers.views import customer_blueprint
from src.ui.models.schedules.views import schedule_blueprint
from src.ui.models.vehicles.views import vehicle_blueprint

app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def home():
    return render_template("home.html")

"""
*** Register here the blueprints ***
"""
app.register_blueprint(schedule_blueprint, url_prefix="/schedules")
app.register_blueprint(customer_blueprint, url_prefix="/customers")
app.register_blueprint(vehicle_blueprint, url_prefix="/vehicles")
