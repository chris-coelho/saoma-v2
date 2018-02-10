from src.domain.modules.services_catalog_module.service_category_vo import ServiceCategoryValueObject
from src.domain.modules.services_catalog_module.services_catalog_exceptions import ServicesCatalogExceptions


class ServiceCategoryDAO:

    @staticmethod
    def create(name, _id=None):
        service_category = ServiceCategoryValueObject(name=name, _id=_id)

        return service_category if ServiceCategoryDAO.validate(service_category) else None

    @staticmethod
    def create_from_db(entity_as_dict):
        return ServiceCategoryDAO.create(entity_as_dict['name'], entity_as_dict['_id'])

    @staticmethod
    def validate(entity):
        messages = []
        if not entity.name:
            messages.append("Nome obrigatório!")

        if len(messages) == 0:
            return True
        else:
            raise ServicesCatalogExceptions(messages)
