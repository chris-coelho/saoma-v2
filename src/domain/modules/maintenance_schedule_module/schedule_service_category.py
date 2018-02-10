from src.domain.modules.entity_base import EntityBase


class ScheduleServiceCategory(EntityBase):
    def __init__(self, schedule_id, service_category_id, _id=None):
        self.schedule_id = schedule_id
        self.service_category_id = service_category_id
        self._id = super().get_id(_id)
