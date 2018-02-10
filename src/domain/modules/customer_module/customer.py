from src.domain.modules.entity_base import EntityBase


class Customer(EntityBase):
    def __init__(self, doc_id, name, email, _id=None):
        self.doc_id = doc_id
        self.name = name
        self.email = email
        self._id = EntityBase.get_id(_id)

    def __repr__(self):
        return "Entity: {}, Name: {}, CPF: {}, Email: {}, Id: {}"\
            .format(self.__class__.__name__, self.name, self.doc_id, self.email, self._id)
