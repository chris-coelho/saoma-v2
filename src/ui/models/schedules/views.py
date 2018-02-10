from flask import Blueprint, request, render_template, redirect, url_for

from src.application.schedule_app_service import ScheduleAppService
from src.domain.modules.customer_module.customer_exceptions import CustomerExceptions
from src.domain.modules.maintenance_schedule_module.schedule_exceptions import ScheduleExceptions
from src.ui.message_handler import handle_message_error

schedule_blueprint = Blueprint('schedules', __name__)


@schedule_blueprint.route('/index')
def index():
    try:
        schedules = ScheduleAppService().get_schedules_view()
    except ScheduleExceptions as e:
        return handle_message_error(e)
    return render_template('schedules/index.html', view=schedules)


@schedule_blueprint.route('/new', methods=['GET', 'POST'])
def new_schedule():
    if request.method == "POST":
        doc_id = request.form['doc_id']

        try:
            schedule_view = ScheduleAppService().schedule_definition_view(doc_id)
            if schedule_view:
                return render_template('schedules/new_schedule_step2.html', view=schedule_view)
        except CustomerExceptions as e:
            return handle_message_error(e)
        except ScheduleExceptions as e:
            return handle_message_error(e)

    return render_template('schedules/new_schedule_step1.html')


@schedule_blueprint.route('/confirm', methods=['POST'])
def confirm_schedule():
    vehicle_id = request.form.get('vehicles')
    categories = request.form.getlist('categories')
    time_scheduled = request.form.get('available_times')

    try:
        ScheduleAppService().schedule_confirmation(vehicle_id, time_scheduled, categories)
    except ScheduleExceptions as e:
        return handle_message_error(e)

    return redirect(url_for('.index'))

