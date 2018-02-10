import json

from src.domain.modules.entity_base import EntityBase


class Vehicle(EntityBase):
    def __init__(self, plate, owner, model, model_year=None, _id=None):
        self.plate = plate
        self.owner = owner  # customer
        self.model = model
        self.model_year = model_year
        self._id = EntityBase.get_id(_id)

    def __repr__(self):
        return "Entity: {}, Plate: {}, Customer: {}, Model: {}, Year: {}, Id: {}" \
            .format(self.__class__.__name__,
                    self.plate,
                    self.owner.name if self.owner else None,
                    self.model.name if self.model else None,
                    self.model_year,
                    self._id) if self else None

    def as_json(self):
        return json.dumps({
            "plate": self.plate,
            "owner": self.owner.__dict__,
            "model": {
                "name": self.model.name,
                "brand": self.model.brand.__dict__,
                "_id": self.model._id},
            "model_year": self.model_year,
            "_id": self._id
        })
