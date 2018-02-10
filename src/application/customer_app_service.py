from src.application.views.customers_index_view import CustomersIndexView
from src.application.views.vehicle_crud_view import VehicleCRUDView
from src.application.views.vehicles_index_view import VehiclesIndexView
from src.domain.services.customer_service import CustomerService
from src.infra.data.customer.customer_repository import CustomerRepository
from src.infra.data.vehicle.model_repository import ModelRepository
from src.infra.data.vehicle.vehicle_repository import VehicleRepository


class CustomerAppService:
    def __init__(self):
        self.__customer_service = CustomerService(CustomerRepository(),
                                                  VehicleRepository(),
                                                  ModelRepository())

    def get_customer(self, _id):
        return self.__customer_service.get_customer(_id)

    def get_customers_view(self):
        customers = self.__customer_service.get_customers()
        customers_view = []
        for customer in customers:
            vehicles = self.__customer_service.get_vehicles(customer._id)
            customer.number_of_vehicles = len(vehicles) if vehicles else 0
            customers_view.append(customer)
        return CustomersIndexView(customers_view)

    def new_customer(self, doc_id, name, email):
        self.__customer_service.new_customer(doc_id, name, email)

    def upd_customer(self, doc_id, name, email, _id):
        self.__customer_service.upd_customer(doc_id, name, email, _id)

    def del_customer(self, _id):
        self.__customer_service.del_customer(_id)

    def get_vehicle(self, _id):
        return self.__customer_service.get_vehicle(_id)

    def get_vehicle_for_crud_view(self, customer_id=None, vehicle_id=None):
        models = self.__customer_service.get_all_available_models()
        if vehicle_id:
            vehicle = self.__customer_service.get_vehicle(vehicle_id)
            return VehicleCRUDView(vehicle.owner, models, vehicle)
        else:
            owner = self.__customer_service.get_customer(customer_id)
            return VehicleCRUDView(owner, models)

    def get_vehicles_view(self, customer_id):
        vehicles = self.__customer_service.get_vehicles(customer_id)
        if vehicles:
            owner = vehicles[0].owner
        else:
            owner = self.__customer_service.get_customer(customer_id)
        return VehiclesIndexView(owner, vehicles)

    def new_vehicle(self, plate, customer_id, model_id, model_year):
        self.__customer_service.new_vehicle(plate, customer_id, model_id, model_year)

    def upd_vehicle(self, plate, customer_id, model_id, model_year, _id):
        self.__customer_service.upd_vehicle(plate, customer_id, model_id, model_year, _id)

    def del_vehicle(self, _id):
        self.__customer_service.del_vehicle(_id)

