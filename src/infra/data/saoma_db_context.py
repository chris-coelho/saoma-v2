import json

import os

from src.infra.data._mongo.mongo_db_context import MongoDbContext


class SaomaDbContext:
    DB_CONTEXT_CLASS = MongoDbContext  # put here another db context depending on db type. Sample: PostgresDbContext
    USERNAME = None
    PASSWORD = None
    HOST = None
    DATABASE_NAME = None
    CONTEXT = None

    @staticmethod
    def get_context():
        if SaomaDbContext.CONTEXT is None:
            SaomaDbContext.__set_db_configuration()
            context = SaomaDbContext.DB_CONTEXT_CLASS()
            SaomaDbContext.CONTEXT = context.get_context(SaomaDbContext.HOST,
                                                         SaomaDbContext.DATABASE_NAME,
                                                         SaomaDbContext.USERNAME,
                                                         SaomaDbContext.PASSWORD)
        return SaomaDbContext.CONTEXT

    @staticmethod
    def __set_db_configuration():
        config_file = '../../db/database.cfg'  # from UI layer
        #config_file = 'db/database.cfg'  # from root

        with open(config_file, 'r') as f:
            cfg = json.load(f)

            if not cfg['username'] or len(cfg['username']) == 0:
                # Remote Server
                SaomaDbContext.HOST = os.environ.get("MONGOLAB_URI")
                SaomaDbContext.DATABASE_NAME = cfg['database_name']
            else:
                SaomaDbContext.USERNAME = cfg['username']
                SaomaDbContext.PASSWORD = cfg['password']
                SaomaDbContext.HOST = cfg['host'].format(SaomaDbContext.USERNAME, SaomaDbContext.PASSWORD)
                SaomaDbContext.DATABASE_NAME = cfg['database_name']

