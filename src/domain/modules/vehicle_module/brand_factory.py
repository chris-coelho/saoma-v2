from src.domain.modules.factory_base import FactoryBase
from src.domain.modules.vehicle_module.brand import Brand
from src.domain.modules.vehicle_module.brand_exceptions import BrandExceptions


class BrandFactory(FactoryBase):

    @staticmethod
    def create(name, _id=None):
        brand = Brand(name=name, _id=_id)

        return brand if BrandFactory.validate(brand) else None

    @staticmethod
    def create_from_db(entity_as_dict):
        return BrandFactory.create(entity_as_dict['name'], entity_as_dict['_id'])

    @staticmethod
    def validate(entity):
        messages = []
        if not entity.name:
            messages.append("Nome obrigatório.")

        if len(entity.name) < 2:
            messages.append("Nome muito curto.")

        if len(messages) == 0:
            return True
        else:
            raise BrandExceptions(messages)
