import pymongo


class MongoDbContext:

    def get_context(self, host, database_name, username, password):
        if not username:
            uri = host
        else:
            uri = host.format(username, password)
        client = pymongo.MongoClient(uri)
        return client[database_name]
