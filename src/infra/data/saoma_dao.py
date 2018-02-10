from src.infra.data._mongo.mongo_repository import MongoRepository
from src.infra.data.saoma_db_context import SaomaDbContext


class SaomaDAO(MongoRepository):
    def __init__(self,
                 collection_name,
                 factory,
                 entity_not_found_exception):

        super().__init__(SaomaDbContext.get_context(), collection_name)
        self.__factory = factory
        self.__entity_not_found_exception = entity_not_found_exception

    def get_by_id(self, _id):
        record = super().get_by_id(_id)
        if not record:
            raise self.__entity_not_found_exception(_id)
        return self._convert_to_entity(record)

    def get_all(self, query=(lambda x: x)):
        return [self._convert_to_entity(data)
                for data
                in super().search(query)]

    def _convert_to_entity(self, json):
        return self.__factory.create_from_db(json) if json else None
