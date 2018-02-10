from src.domain.modules.customer_module.customer_factory import CustomerFactory
from src.domain.modules.vehicle_module.vehicle_factory import VehicleFactory


class CustomerService:
    def __init__(self, customer_repo, vehicle_repo=None, model_repo=None):
        self.__customer_repo = customer_repo
        self.__vehicle_repo = vehicle_repo
        self.__model_repo = model_repo

    def get_customer(self, _id):
        return self.__customer_repo.get_by_id(_id)

    def new_customer(self, doc_id, name, email):
        self.__customer_repo.add(CustomerFactory.create(doc_id, name, email))

    def upd_customer(self, doc_id, name, email, _id):
        self.__customer_repo.update(CustomerFactory.create(doc_id, name, email, _id))

    def del_customer(self, _id):
        self.__customer_repo.delete(_id)

    def get_customers(self):
        return self.__customer_repo.get_all()

    def get_customer_by_doc(self, doc_id):
        return self.__customer_repo.get_by_doc_id(doc_id)

    def get_vehicle(self, _id):
        return self.__vehicle_repo.get_by_id(_id)

    def new_vehicle(self, plate, customer_id, model_id, model_year):
        self.__vehicle_repo.add(
            self.__get_vehicle(plate, customer_id, model_id, model_year))

    def upd_vehicle(self, plate, customer_id, model_id, model_year, _id):
        self.__vehicle_repo.update(
            self.__get_vehicle(plate, customer_id, model_id, model_year, _id))

    def del_vehicle(self, _id):
        if self.__vehicle_repo_supplied():
            self.__vehicle_repo.delete(_id)

    def get_vehicles(self, customer_id):
        if self.__vehicle_repo_supplied():
            return self.__vehicle_repo.get_vehicles_by_customer(customer_id)

    def get_all_available_models(self, brand_id=None):
        if brand_id:
            return self.__model_repo.get_all()
        else:
            return self.__model_repo.get_all()

    def __vehicle_repo_supplied(self):
        if not self.__vehicle_repo:
            raise ValueError("Vehicle repository is required as parameter to CustomerService")
        return True

    def __model_repo_supplied(self):
        if not self.__model_repo:
            raise ValueError("Model repository is required as parameter to CustomerService")
        return True

    def __get_vehicle(self, plate, customer_id, model_id, model_year, _id=None):
        owner = self.__customer_repo.get_by_id(customer_id)
        model = self.__model_repo.get_by_id(model_id)
        return VehicleFactory.create(plate, owner, model, model_year, _id)
