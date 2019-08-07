from aicyber.com.data_channel.utils.Util import Utils
import importlib


class ModifyHandler(object):
    __datasourceConnectionPool=None
    __targetdatasourceConnectionPool=None
    __dbtypes={}
    __conf=None

    def __init__(self):
        util=Utils()
        self.__conf=util.getConf()

    async def init(self):
        await self.__initConnection(self.__conf)

    def getDataSourceTables(self):
        pass

    def getTargetDataSourceTables(self):
        pass

    def __verifyDB(self,conf):
        f_dbtype=conf['from'].get('db_type')
        t_dbtype=conf['to'].get('db_type')
        if f_dbtype=='mysql':
            self.__dbtypes['from']='mysql'
        if t_dbtype=='postgresql':
            self.__dbtypes['to']='postgresql'

    async def __getPools(self):
        pools={}
        f_type=self.__dbtypes['from']
        t_type=self.__dbtypes['to']
        f_pool=await self.generateFromConn(f_type)
        t_pool=await self.generateToConn(t_type)
        pools['from']=f_pool
        pools['to']=t_pool
        return pools

    def generateFromConn(self,type):
        if type == 'mysql':
            # module = importlib.import_module('..DB_Driver.mysql', './DB_Driver')
            module = importlib.import_module('.mysql', 'DB_Driver')
            conn = getattr(module, 'MySQL')
            return conn(self.__conf['from']).getMySQLConnection()
        if type == 'postgresql':
            module = importlib.import_module('.postgresql', 'DB_Driver')
            pool = getattr(module, 'PostgreSQL')
            return pool(self.__conf['from']).getPgConnection()

    def generateToConn(self,type):
        if type == 'mysql':
            # module = importlib.import_module('..DB_Driver.mysql', './DB_Driver')
            module = importlib.import_module('.mysql', 'DB_Driver')
            conn = getattr(module, 'MySQL')
            return conn(self.__conf['to']).getMySQLConnection()
        if type == 'postgresql':
            module = importlib.import_module('.postgresql', 'DB_Driver')
            pool = getattr(module, 'PostgreSQL')
            return pool(self.__conf['to']).getPgConnection()

    async def __initConnection(self,conf):
        self.__verifyDB(conf)
        pools=await self.__getPools()
        self.__datasourceConnectionPool=pools['from']
        self.__targetdatasourceConnectionPool=pools['to']

    def getPools(self):
        dic={}
        dic['from_pool']=self.__datasourceConnection
        dic['to_pool']=self.__targetdatasourceConnection
        return dic

    def getFromPool(self):
        return self.__datasourceConnectionPool

    def getToPool(self):
        return self.__targetdatasourceConnectionPool

    def getConf(self):
        return self.__conf
