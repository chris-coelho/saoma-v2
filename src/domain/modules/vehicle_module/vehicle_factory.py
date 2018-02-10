from src.domain.modules.factory_base import FactoryBase
from src.domain.modules.vehicle_module.model import Model
from src.domain.modules.vehicle_module.vehicle import Vehicle
from src.domain.modules.vehicle_module.vehicle_exceptions import VehicleExceptions


class VehicleFactory(FactoryBase):

    @staticmethod
    def create(plate, owner, model, model_year=None, _id=None):
        vehicle = Vehicle(plate=plate,
                          owner=owner,
                          model=model,
                          model_year=model_year,
                          _id=_id)

        return vehicle if VehicleFactory.validate(vehicle) else None

    @staticmethod
    def create_from_db(entity_as_dict):
        return VehicleFactory.create(entity_as_dict['plate'],
                                     entity_as_dict['owner'],
                                     entity_as_dict['model'],
                                     entity_as_dict['model_year'],
                                     entity_as_dict['_id'])

    @staticmethod
    def validate(entity):
        messages = []
        if not entity.plate:
            messages.append("Placa obrigatória!")
        if not entity.model:
            messages.append("Modelo obrigatório!")

        if len(messages) == 0:
            return True
        else:
            raise VehicleExceptions(messages)
