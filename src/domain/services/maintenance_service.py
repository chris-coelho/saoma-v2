from datetime import datetime

from src.domain.modules.maintenance_schedule_module.schedule_factory import ScheduleFactory
from src.domain.modules.maintenance_schedule_module.schedule_manager import ScheduleManager


class MaintenanceService:
    def __init__(self, schedule_repo, vehicle_repo, services_catalog_dao):
        self.__schedule_repo = schedule_repo
        self.__vehicle_repo = vehicle_repo
        self.__services_catalog_dao = services_catalog_dao
        self.__schedule_manager = ScheduleManager(schedule_repo)

    def get_available_times(self):
        return self.__schedule_manager.get_available_times()

    def register_schedule(self, vehicle_id, time_scheduled, service_categories):
        schedule = ScheduleFactory.create(self.__vehicle_repo.get_by_id(vehicle_id),
                                          datetime.strptime(time_scheduled, '%Y-%m-%d %H:%M:%S'),  # YYYY-MM-DD HH:MM:SS
                                          [self.__services_catalog_dao.get_by_id(c) for c in service_categories])
        self.__schedule_repo.add(schedule)

    def get_schedules(self, start_date=None):
        if start_date:
            return self.__schedule_repo.get_all(lambda sd: sd['time_scheduled'] >= start_date)
        return self.__schedule_repo.get_all()
