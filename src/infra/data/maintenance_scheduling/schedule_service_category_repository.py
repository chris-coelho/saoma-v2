from src.domain.modules.maintenance_schedule_module.schedule_exceptions import ScheduleExceptions
from src.domain.modules.maintenance_schedule_module.schedule_service_category_factory import \
    ScheduleServiceCategoryFactory
from src.infra.data.saoma_repository import SaomaRepository


class ScheduleServiceCategoriesRepository(SaomaRepository):
    def __init__(self):
        super().__init__(collection_name="schedule_service_categories",
                         factory=ScheduleServiceCategoryFactory,
                         entity_not_found_exception=ScheduleExceptions,
                         entity_already_exists_exception=ScheduleExceptions)

