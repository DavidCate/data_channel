import aiomysql
import asyncio

class MySQL():
    __conf=None

    def __init__(self,conf):
        self.__conf=conf

    async def getMySQLConnection(self):
        loop=asyncio.get_running_loop()
        mysql_poll=await aiomysql.create_pool(
            host=self.__conf.get('host'),
            port=self.__conf.get('port'),
            user=self.__conf.get('user'),
            password=self.__conf.get('pwd'),
            db=self.__conf.get('database'),
            loop=loop
        )
        return mysql_poll

