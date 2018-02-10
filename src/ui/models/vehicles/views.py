from flask import Blueprint, request, render_template, redirect, url_for

from src.application.customer_app_service import CustomerAppService
from src.domain.modules.vehicle_module.vehicle_exceptions import VehicleExceptions

vehicle_blueprint = Blueprint('vehicles', __name__)


@vehicle_blueprint.route('/index/<string:customer_id>')
def index(customer_id):
    vehicles_view = CustomerAppService().get_vehicles_view(customer_id)
    return render_template('vehicles/index.html', view=vehicles_view)


@vehicle_blueprint.route('/new/<string:owner_id>', methods=['GET', 'POST'])
def new_vehicle(owner_id):
    if request.method == 'POST':
        plate = request.form['plate']
        model_id = request.form.get('models')
        model_year = request.form['model_year']

        try:
            CustomerAppService().new_vehicle(plate, owner_id, model_id, model_year)
            return redirect(url_for('.index', customer_id=owner_id))
        except VehicleExceptions as e:
            return e.args

    return render_template('vehicles/new_vehicle.html',
                           view=CustomerAppService().get_vehicle_for_crud_view(customer_id=owner_id))


@vehicle_blueprint.route('/edit/<string:vehicle_id>', methods=['GET', 'POST'])
def upd_vehicle(vehicle_id):
    if request.method == 'POST':
        owner_id = request.form['owner_id']
        plate = request.form['plate']
        model_id = request.form.get('models')
        model_year = request.form['model_year']

        try:
            CustomerAppService().upd_vehicle(plate, owner_id, model_id, model_year, vehicle_id)
            return redirect(url_for('.index', customer_id=owner_id))
        except VehicleExceptions as e:
            return e.args

    return render_template('vehicles/upd_vehicle.html',
                           view=CustomerAppService().get_vehicle_for_crud_view(vehicle_id=vehicle_id))



