import pymongo


class MongoDbContext:

    def get_context(self, host, database_name, username, password):
        if not username:
            client = pymongo.MongoClient(host)
            context = client.get_default_database()
        else:
            uri = host.format(username, password)
            client = pymongo.MongoClient(uri)
            context = client[database_name]
        return context
