from src.domain.modules.services_catalog_module.service_category_dao import ServiceCategoryDAO
from src.domain.modules.services_catalog_module.service_category_vo import ServiceCategoryValueObject
from src.domain.modules.services_catalog_module.services_catalog_exceptions import ServiceCategoryNotFoundException
from src.infra.data.saoma_dao import SaomaDAO


class ServicesCatalogDAO(SaomaDAO):
    def __init__(self):
        super().__init__(collection_name="service_categories",
                         factory=ServiceCategoryDAO,
                         entity_not_found_exception=ServiceCategoryNotFoundException)

    def get_service_categories(self):
        categories = super().search()
        return [ServiceCategoryValueObject(**category)
                for category
                in categories] if categories else None
