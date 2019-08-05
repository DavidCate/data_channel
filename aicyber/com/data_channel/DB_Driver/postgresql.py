import asyncpg

class PostgreSQL():
    __conf=None
    __pg_connection=None

    def __init__(self,conf):
        self.__conf=conf
        self.setPgConnection()


    async def setPgConnection(self):
        self.__pg_connection=await asyncpg.create_pool(
            self.__conf
        )

