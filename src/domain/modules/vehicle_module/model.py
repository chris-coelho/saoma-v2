import json

from src.domain.modules.entity_base import EntityBase


class Model(EntityBase):
    def __init__(self, name, brand, _id=None):
        self.name = name
        self.brand = brand
        self._id = EntityBase.get_id(_id)

    def __repr__(self):
        return "Entity: {}, Name: {}, Brand: {}, Id: {}"\
            .format(self.__class__.__name__,
                    self.name,
                    self.brand.name if self.brand else None,
                    self._id)

    def as_json(self):
        return json.dumps({
            "name": self.name,
            "brand": self.brand.__dict__,
            "_id": self._id,
        })
