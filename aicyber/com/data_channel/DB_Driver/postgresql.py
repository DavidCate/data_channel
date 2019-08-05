import asyncpg

class PostgreSQL():
    __conf=None
    __pg_connection=None

    def __init__(self,conf):
        self.__conf=conf
        self.setPgConnection()


    def setPgConnection(self):
        pass

