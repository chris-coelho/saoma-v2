

class ServicesCatalogService:
    def __init__(self, service_catalog_dao):
        self.__service_catalog_dao = service_catalog_dao

    def get_service_categories(self):
        return self.__service_catalog_dao.get_service_categories()

