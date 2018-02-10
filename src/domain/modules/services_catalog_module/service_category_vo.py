import json
import uuid


class ServiceCategoryValueObject:
    def __init__(self, name, _id=None):
        self.name = name
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "VO: {}, Name: {}, Id: {}".format(self.__class__.__name__,
                                                 self.name,
                                                 self._id)

    def as_json(self):
        return json.dumps(self.__dict__)
