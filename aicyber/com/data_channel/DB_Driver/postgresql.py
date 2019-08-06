import asyncpg

class PostgreSQL():
    __conf=None
    __pg_connection=None

    def __init__(self,conf):
        self.__conf=conf
        self.setPgConnection()


    def setPgConnection(self):
        self.__pg_connection=asyncpg.create_pool(
            host=self.__conf.get('host'),
            port=self.__conf.get('port'),
            user=self.__conf.get('user'),
            password=self.__conf.get('pwd'),
            database=self.__conf.get('database'),
            max_size=100
        )

