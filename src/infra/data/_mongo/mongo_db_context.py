import pymongo


class MongoDbContext:
    def get_context(self, host, database_name, username, password):
        uri = host.format(username, password)
        client = pymongo.MongoClient(uri)
        return client[database_name]
