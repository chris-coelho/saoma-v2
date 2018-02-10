from src.domain.modules.factory_base import FactoryBase
from src.domain.modules.maintenance_schedule_module.schedule import Schedule
from src.domain.modules.maintenance_schedule_module.schedule_exceptions import ScheduleExceptions


class ScheduleFactory(FactoryBase):

    @staticmethod
    def create(vehicle, time_scheduled, service_categories, _id=None):
        schedule = Schedule(vehicle=vehicle,
                            time_scheduled=time_scheduled,
                            service_categories=service_categories,
                            _id=_id)

        return schedule if ScheduleFactory.validate(schedule) else None

    @staticmethod
    def create_from_db(entity_as_dict):
        return ScheduleFactory.create(entity_as_dict['vehicle'],
                                      entity_as_dict['time_scheduled'],
                                      entity_as_dict['service_categories'],
                                      entity_as_dict['_id'])

    @staticmethod
    def validate(entity):
        messages = []
        if not entity.vehicle:
            messages.append("Veículo obrigatório!")
        if not entity.time_scheduled:
            messages.append("Dia/Horário obrigatório!")

        if len(messages) == 0:
            return True
        else:
            raise ScheduleExceptions(messages)
