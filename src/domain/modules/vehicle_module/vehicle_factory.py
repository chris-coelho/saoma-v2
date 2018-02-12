import datetime

import re

from src.domain.modules.factory_base import FactoryBase
from src.domain.modules.vehicle_module.vehicle import Vehicle
from src.domain.modules.vehicle_module.vehicle_exceptions import VehicleExceptions


class VehicleFactory(FactoryBase):

    @staticmethod
    def create(plate, owner, model, model_year=None, _id=None):
        vehicle = Vehicle(plate=plate,
                          owner=owner,
                          model=model,
                          model_year=model_year,
                          _id=_id)

        return vehicle if VehicleFactory.validate(vehicle) else None

    @staticmethod
    def create_from_db(entity_as_dict):
        return VehicleFactory.create(entity_as_dict['plate'],
                                     entity_as_dict['owner'],
                                     entity_as_dict['model'],
                                     entity_as_dict['model_year'],
                                     entity_as_dict['_id'])

    @staticmethod
    def validate(entity):
        messages = []
        if not entity.plate:
            messages.append("Placa obrigatória!")
        else:
            entity.plate = entity.plate.upper()
            if not re.match(r"(^([a-z]{3}|[A-Z]{3})+([0-9]{4})$)", entity.plate):
                messages.append("Placa {} deve ter o formato: AAA1234".format(entity.plate))

        if not entity.model:
            messages.append("Modelo obrigatório!")

        if entity.model_year:
            year_as_string = ''.join(re.findall('\d', str(entity.model_year)))
            if not year_as_string or len(year_as_string) != 4:
                messages.append("Ano modelo {} inválido para o automóvel placas {}. Informe apenas números"
                                .format(entity.model_year, entity.plate))
            else:
                entity.model_year = int(year_as_string)
                if entity.model_year < 1900:
                    messages.append("Ano modelo {} inválido para o automóvel placas {}. "
                                    "Mínimo permitido: 1900".format(entity.model_year, entity.plate))

                if entity.model_year > datetime.date.today().year + 1:
                    messages.append("Ano modelo {} inválido para o automóvel placas {}. "
                                    "Máximo permitido: ano atual + 1 ano".format(entity.model_year, entity.plate))

        if len(messages) == 0:
            return True
        else:
            raise VehicleExceptions(messages)
