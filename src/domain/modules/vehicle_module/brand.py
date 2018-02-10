from src.domain.modules.entity_base import EntityBase


class Brand(EntityBase):
    def __init__(self, name, _id=None):
        self.name = name
        self._id = EntityBase.get_id(_id)

    def __repr__(self):
        return "Entity: {}, Name: {}, Id: {}" \
            .format(self.__class__.__name__, self.name, self._id)
