from src.infra.data.repository_base import RepositoryBase


class MongoRepository(RepositoryBase):
    def __init__(self, context, collection_name):
        self.__collection = context[collection_name]

    def add(self, document):
        self.__collection.insert(document)

    def update(self, document):
        self.__collection.update({'_id': document['_id']}, document)

    def delete(self, document):
        self.__collection.remove({'_id': document['_id']})

    def get_by_id(self, _id):
        return self.__collection.find_one({'_id': _id})

    def search(self, query=(lambda x: x)):
        data = self.__collection.find({})
        return [x for x in data if query(x)]
