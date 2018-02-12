from flask import Blueprint, request, render_template, redirect, url_for

from src.application.customer_app_service import CustomerAppService
from src.domain.modules.customer_module.customer_exceptions import CustomerExceptions
from src.domain.modules.vehicle_module.vehicle_exceptions import VehicleExceptions
from src.ui.message_handler import handle_message_error

customer_blueprint = Blueprint('customers', __name__)


@customer_blueprint.route('/index')
def index():
    try:
        customers = CustomerAppService().get_customers_view()
    except CustomerExceptions as e:
        return handle_message_error(e)
    except VehicleExceptions as e:
        return handle_message_error(e)
    return render_template('customers/index.html', view=customers)


@customer_blueprint.route('/new', methods=['GET', 'POST'])
def new_customer():
    if request.method == 'POST':
        doc_id = request.form['doc_id']
        name = request.form['name']
        email = request.form['email']

        try:
            CustomerAppService().new_customer(doc_id, name, email)
            return redirect(url_for('.index'))
        except CustomerExceptions as e:
            return handle_message_error(e)

    return render_template('customers/new_customer.html')


@customer_blueprint.route('/edit/<string:customer_id>', methods=['GET', 'POST'])
def upd_customer(customer_id):
    if request.method == 'POST':
        doc_id = request.form['doc_id']
        name = request.form['name']
        email = request.form['email']

        try:
            CustomerAppService().upd_customer(doc_id, name, email, customer_id)
            return redirect(url_for('.index'))
        except CustomerExceptions as e:
            return handle_message_error(e)

    return render_template('customers/upd_customer.html', view=CustomerAppService().get_customer(customer_id))
