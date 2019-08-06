import asyncpg

class PostgreSQL():
    __conf=None

    def __init__(self,conf):
        self.__conf=conf

    async def getPgConnection(self):
        pg_poll=await asyncpg.create_pool(
            host=self.__conf.get('host'),
            port=self.__conf.get('port'),
            user=self.__conf.get('user'),
            password=self.__conf.get('pwd'),
            database=self.__conf.get('database'),
            max_size=100
        )
        return pg_poll

