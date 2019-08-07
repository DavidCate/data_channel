from aicyber.com.data_channel.ModifyHandler import ModifyHandler
from aicyber.com.data_channel.Tasks import Tasks
from aicyber.com.data_channel.Task import Task
from aicyber.com.data_channel.Sqls import Sqls
from typing import TypeVar, Generic


class BaseHandler(ModifyHandler):
    tasks = Tasks()

    async def execTasks(self, tasks: Tasks):
        await self.init()
        tasks = tasks.getTasks()
        for task in tasks:
            await self.execTask(task)

    async def execTask(self, task: Task):
        select_sql = self.generate_selectsql_by_task(task)
        res=await self.exec_query(select_sql)
        insert_sql=self.generate_insertsql_by_task(task,res)
        r=await self.exec_insert(insert_sql)

    async def exec_insert(self,insert_sql):
        db_type = self.getConf()['to'].get('db_type')
        if db_type=='mysql':
            res=await self.exec_mysql_insert(insert_sql)
        if db_type=='postgresql':
            res=await self.exec_postgresql_insert(insert_sql)
        if db_type=='oracle':
            res=await self.exec_oracle_insert(insert_sql)
        return res

    async def exec_mysql_insert(self,sql):
        pass

    async def exec_postgresql_insert(self,sql):
        pass

    async def exec_oracle_insert(self,sql):
        pass


    def generate_insertsql_by_task(self,task,res):
        db_type=self.getConf()['to'].get('db_type')
        insertTable=task.getInsertTable()
        insertFields=task.getInsertFields()
        if db_type=='mysql':
            sql=self.generate_mysql_insertsql(insertTable,insertFields,res)
        if db_type=='postgresql':
            sql=self.generate_postgresql_insertsql(insertTable,insertFields,res)
        if db_type=='oracle':
            sql=self.generate_oracle_insertsql(insertTable,insertFields,res)
        return sql

    def generate_mysql_insertsql(self,table:str,fields:list,res):
        pass

    def generate_postgresql_insertsql(self, table: str, fields: list, res):
        pass

    def generate_oracle_insertsql(self,table:str,fields:list,res):
        pass

    async def exec_query(self,sql):
        db_type=self.getConf()['from'].get('db_type')
        if db_type=='mysql':
            res=await self.exec_mysql_query(sql)
        if db_type=='postgresql':
            res=await self.exec_postgresql_query(sql)
        if db_type=='oracle':
            res=await self.exec_oracle_query(sql)
        return res



    async def exec_mysql_query(self,sql):
        pass

    async def exec_postgresql_query(self,sql):
        async with self.getFromPool().acquire() as conn:
            res = await conn.fetch(sql)
            res = [dict(r) for r in res]
        return res


    async def exec_oracle_query(self,sql):
        pass

    def generate_selectsql_by_task(self, task):
        db_type=self.getConf()['from'].get('db_type')
        selecTable = task.getSelectTable()
        selectFiles = task.getSelectFiles()
        if db_type=='mysql':
            selectsql =self.generate_mysql_select_sql(selecTable,selectFiles)
        if db_type=='postgresql':
            selectsql =self.generate_postgresql_select_sql(selecTable,selectFiles)
        if db_type=='oracle':
            selectsql =self.generate_oracle_select_sql(selecTable,selectFiles)
        return selectsql

    def generate_mysql_select_sql(self, table: str, fiels: list):
        fiels_concat=''
        for fiel in fiels:
            fiels_concat+='`'+fiel+'`'+','
        fiels_concat=fiels_concat[:len(fiels_concat)-1]
        sql='select {fiels} from {table}'
        sql=sql.format(fiels=fiels_concat,table=table)
        print(sql)
        return sql


    def generate_postgresql_select_sql(self,table:str,fiels:list):
        fiels_concat = ''
        for fiel in fiels:
            fiels_concat += '\"' + fiel + '\"' + ','
        fiels_concat = fiels_concat[:len(fiels_concat) - 1]
        sql = 'select {fiels} from {table}'
        sql.format(fiels_concat, table)
        print(sql)
        return sql

    def generate_oracle_select_sql(self,table:str,fiels:list):
        pass

    def generate_insert_sql(self, table: str, fiels: list, values: list):
        pass

    def onHandleMethod(self):
        pass

    async def select(self, sql):
        await self.init()
        to_pool=self.getToPool()
        async with to_pool.acquire() as conn:
            res = await conn.fetch(sql)
            res= [dict(r) for r in res]
            return res


    def insert(self, sql):
        pass

    def getTableFields(self,tableName:str):
        pass
