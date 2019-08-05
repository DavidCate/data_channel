import aiomysql

class MySQL():
    __conf=None

    def __init__(self,conf):
        self.__conf=conf

