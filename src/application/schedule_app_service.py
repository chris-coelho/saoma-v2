from datetime import datetime

from src.application.views.schedule_definition_view import ScheduleDefinitionView
from src.application.views.schedules_index_view import SchedulesIndexView
from src.domain.services.customer_service import CustomerService
from src.domain.services.maintenance_service import MaintenanceService
from src.domain.services.services_catalog_service import ServicesCatalogService
from src.infra.data.customer.customer_repository import CustomerRepository
from src.infra.data.maintenance_scheduling.schedule_repository import ScheduleRepository
from src.infra.data.services_catalog.services_catalog_dao import ServicesCatalogDAO
from src.infra.data.vehicle.vehicle_repository import VehicleRepository


class ScheduleAppService:
    def __init__(self):
        self.__customer_service = CustomerService(CustomerRepository(),
                                                  VehicleRepository())
        self.__services_catalog_service = ServicesCatalogService(ServicesCatalogDAO())
        self.__maintenance_service = MaintenanceService(ScheduleRepository(),
                                                        VehicleRepository(),
                                                        ServicesCatalogDAO())

    def schedule_definition_view(self, customer_doc):
        customer = self.__customer_service.get_customer_by_doc(customer_doc)
        vehicles = self.__customer_service.get_vehicles(customer._id)
        service_categories = self.__services_catalog_service.get_service_categories()
        available_times = self.__maintenance_service.get_available_times()

        return ScheduleDefinitionView(customer, vehicles, service_categories, available_times)

    def schedule_confirmation(self, vehicle_id, time_scheduled, service_categories):
        self.__maintenance_service.register_schedule(vehicle_id, time_scheduled, service_categories)
        return True

    def get_schedules_view(self):
        schedules = self.__maintenance_service.get_schedules(datetime.today())
        schedules = sorted(schedules, key=lambda s: s.time_scheduled)
        schedules_view = []
        for schedule in schedules:
            services_name = ", ".join([category.name for category in schedule.service_categories])
            schedules_view.append(SchedulesIndexView(schedule.time_scheduled, schedule.vehicle, services_name))

        return schedules_view
