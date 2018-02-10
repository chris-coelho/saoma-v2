from src.domain.modules.factory_base import FactoryBase
from src.domain.modules.vehicle_module.brand import Brand
from src.domain.modules.vehicle_module.model import Model
from src.domain.modules.vehicle_module.model_exceptions import ModelExceptions


class ModelFactory(FactoryBase):

    @staticmethod
    def create(name, brand, _id=None):
        model = Model(name=name, brand=brand, _id=_id)
        return model if ModelFactory.validate(model) else None

    @staticmethod
    def create_from_db(entity_as_dict):
        return ModelFactory.create(entity_as_dict['name'], entity_as_dict['brand'], entity_as_dict['_id'])

    @staticmethod
    def validate(entity):
        messages = []
        if not entity.name:
            messages.append("Nome obrigatório!")
        if not entity.brand or not isinstance(entity.brand, Brand):
            messages.append("Marca obrigatória!")

        if len(messages) == 0:
            return True
        else:
            raise ModelExceptions(messages)
