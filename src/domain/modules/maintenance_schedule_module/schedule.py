from src.domain.modules.entity_base import EntityBase


class Schedule(EntityBase):
    def __init__(self, vehicle, time_scheduled, service_categories=None, _id=None):
        self.vehicle = vehicle
        self.service_categories = service_categories
        self.time_scheduled = time_scheduled
        self._id = EntityBase.get_id(_id)

    def __repr__(self):
        return "Entity: {}, Vehicle Id: {}, Categories: {}, Time Scheduled: {}, Id: {}"\
            .format(self.__class__.__name__, self.vehicle.model, self.service_categories, self.time_scheduled, self._id)

