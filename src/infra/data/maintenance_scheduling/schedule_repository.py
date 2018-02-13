from src.domain.modules.maintenance_schedule_module.schedule_exceptions import ScheduleNotFoundException, \
    ScheduleAlreadyExistsException
from src.domain.modules.maintenance_schedule_module.schedule_factory import ScheduleFactory
from src.domain.modules.maintenance_schedule_module.schedule_service_category import ScheduleServiceCategory
from src.infra.data.maintenance_scheduling.schedule_service_category_repository import \
    ScheduleServiceCategoriesRepository
from src.infra.data.saoma_repository import SaomaRepository
from src.infra.data.services_catalog.services_catalog_dao import ServicesCatalogDAO
from src.infra.data.vehicle.vehicle_repository import VehicleRepository


class ScheduleRepository(SaomaRepository):
    def __init__(self):
        super().__init__(collection_name="schedules",
                         factory=ScheduleFactory,
                         entity_not_found_exception=ScheduleNotFoundException,
                         entity_already_exists_exception=ScheduleAlreadyExistsException)
        self.__vehicle_repo = VehicleRepository()
        self.__services_catalog_dao_repo = ServicesCatalogDAO()
        self.__schedule_service_categories_repo = ScheduleServiceCategoriesRepository()

    def get_blocked_times(self, start_date, end_date):
        data = super().search(lambda x: start_date <= x['time_scheduled'] <= end_date)
        return [d['time_scheduled'] for d in data] if data else None

    def add(self, entity):
        if entity.service_categories:
            """ save all service categories for this scheduling """
            for category in entity.service_categories:
                schedule_sc = ScheduleServiceCategory(entity._id, category._id)
                self.__schedule_service_categories_repo.add(schedule_sc)
        super().add(entity)

    def get_all(self, query=(lambda x: x)):
        return [self._convert_to_entity(data)
                for data
                in super().search(query)]

    def _convert_to_entity(self, json):
        if not json:
            return None

        vehicle = self.__vehicle_repo.get_by_id(json['vehicle_id'])
        service_categories = [self.__services_catalog_dao_repo.get_by_id(data.service_category_id)
                              for data
                              in self.__schedule_service_categories_repo.get_all(
                                    lambda x: x['schedule_id'] == json['_id'])]

        return ScheduleFactory.create_from_db({'vehicle': vehicle,
                                               'time_scheduled': json['time_scheduled'],
                                               'service_categories': service_categories,
                                               '_id': json['_id']})

    """
    - service categories will be saved through add method in this class in another collection/table db
    """
    def _as_record(self, entity):
        return {
            '_id': entity._id,
            'vehicle_id': entity.vehicle._id,
            'time_scheduled': entity.time_scheduled,
        }
