from src.infra.data._mongo.mongo_repository import MongoRepository
from src.infra.data.saoma_db_context import SaomaDbContext


class SaomaRepository(MongoRepository):  # inheritance from another db repo depending on db. Sample: PostgresRepository
    def __init__(self,
                 collection_name,
                 factory,
                 entity_not_found_exception,
                 entity_already_exists_exception):

        super().__init__(SaomaDbContext.get_context(), collection_name)
        self.__factory = factory
        self.__entity_not_found_exception = entity_not_found_exception
        self.__entity_already_exists_exception = entity_already_exists_exception

    def add(self, entity):
        record = super().get_by_id(entity._id)
        if record:
            raise self.__entity_already_exists_exception(entity)
        super().add(self._as_record(entity))

    def update(self, entity):
        record = super().get_by_id(entity._id)
        if not record:
            raise self.__entity_not_found_exception(entity._id)
        super().update(self._as_record(entity))

    def delete(self, _id):
        record = super().get_by_id(_id)
        if not record:
            raise self.__entity_not_found_exception(_id)
        super().delete(self._as_record(record))

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

    def _as_record(self, entity):
        return entity.__dict__ if entity else None
