from src.domain.modules.vehicle_module.vehicle_exceptions import VehicleNotFoundException, VehicleAlreadyExistsException
from src.domain.modules.vehicle_module.vehicle_factory import VehicleFactory
from src.infra.data.saoma_repository import SaomaRepository
from src.infra.data.vehicle.model_repository import ModelRepository
from src.infra.data.customer.customer_repository import CustomerRepository


class VehicleRepository(SaomaRepository):
    def __init__(self):
        super().__init__(collection_name="vehicles",
                         factory=VehicleFactory,
                         entity_not_found_exception=VehicleNotFoundException,
                         entity_already_exists_exception=VehicleAlreadyExistsException)
        self.__customer_repo = CustomerRepository()
        self.__model_repo = ModelRepository()

    def get_vehicles_by_customer(self, customer_id):
        return [self._convert_to_entity(data)
                for data
                in super().search(lambda x: x['owner_id'] == customer_id)]

    def _convert_to_entity(self, json):
        if not json:
            return None

        owner = self.__customer_repo.get_by_id(json['owner_id'])
        model = self.__model_repo.get_by_id(json['model_id'])

        return VehicleFactory.create_from_db({'_id': json['_id'],
                                              'plate': json['plate'],
                                              'owner': owner,
                                              'model': model,
                                              'model_year': json['model_year']})

    def _as_record(self, entity):
        return {
            '_id': entity._id,
            'plate': entity.plate,
            'owner_id': entity.owner._id,
            'model_id': entity.model._id,
            'model_year': entity.model_year,
        }
