from src.domain.modules.factory_base import FactoryBase
from src.domain.modules.maintenance_schedule_module.schedule_service_category import ScheduleServiceCategory


class ScheduleServiceCategoryFactory(FactoryBase):

    @staticmethod
    def create(schedule_id, service_category_id, _id=None):
        schedule_service_category = ScheduleServiceCategory(schedule_id=schedule_id,
                                                            service_category_id=service_category_id,
                                                            _id=_id)

        return schedule_service_category \
            if ScheduleServiceCategoryFactory.validate(schedule_service_category) else None

    @staticmethod
    def create_from_db(entity_as_dict):
        return ScheduleServiceCategoryFactory.create(entity_as_dict['schedule_id'],
                                                     entity_as_dict['service_category_id'],
                                                     entity_as_dict['_id'])

    @staticmethod
    def validate(entity):
        return True
