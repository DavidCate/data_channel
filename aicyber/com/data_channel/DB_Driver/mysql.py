import aiomysql
import asyncio

class MySQL():
    __conf=None
    __mysql_connection=None
    __loop =None

    def __init__(self,conf):
        self.__conf=conf
        self.__loop=asyncio.get_event_loop()

    async def setMySQLConnection(self):
        self.__mysql_connection=await aiomysql.create_pool(
            host=self.__conf.get('host'),
            port=self.__conf.get('port'),
            user=self.__conf.get('user'),
            password=self.__conf.get('pwd'),
            db=self.__conf.get('database'),
            loop=self.__loop
        )