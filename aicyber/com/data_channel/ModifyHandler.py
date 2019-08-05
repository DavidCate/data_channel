from aicyber.com.data_channel.utils.Util import Utils
import importlib
import asyncpg
import aiomysql
from .DB_Driver import mysql

class ModifyHandler(object):
    __datasourceConnection=None
    __targetdatasourceConnection=None
    __dbtypes={}
    __conf=None

    def __init__(self):
        util=Utils()
        self.__conf=util.getConf()
        self.initConnection(self.__conf)

    def getDataSourceTables(self):
        pass

    def getTargetDataSourceTables(self):
        pass

    def verifyDB(self,conf):
        f_dbtype=conf['from'].get('db_type')
        t_dbtype=conf['to'].get('db_type')
        if f_dbtype=='mysql':
            self.__dbtypes['from']='mysql'
        if t_dbtype=='postgresql':
            self.__dbtypes['to']='postgresql'

    def importDriver(self):
        connections={}
        f_type=self.__dbtypes['from']
        t_type=self.__dbtypes['to']
        f_conn=self.generateConn(f_type)
        t_conn=self.generateConn(t_type)
        connections['from']=f_conn
        connections['to']=t_conn
        return connections

    def generateConn(self,type):
        if type == 'mysql':
            # module = importlib.import_module('..DB_Driver.mysql', './DB_Driver')
            module = importlib.import_module('.mysql', 'DB_Driver')
            conn = getattr(module, 'MySQL')
            return conn(self.__conf)
        if type == 'postgresql':
            module = importlib.import_module('.postgresql', 'DB_Driver')
            conn = getattr(module, 'PostgreSQL')
            return conn(self.__conf)





    def initConnection(self,conf):
        self.verifyDB(conf)
        connections=self.importDriver()
        self.__datasourceConnection=connections['from']
        self.__targetdatasourceConnection=connections['to']

    def getConnection(self):
        dic={}
        dic['from_conn']=self.__datasourceConnection
        dic['to_conn']=self.__targetdatasourceConnection
        return dic

    def getConf(self):
        return self.__conf
