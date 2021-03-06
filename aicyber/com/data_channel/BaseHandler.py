from aicyber.com.data_channel.ModifyHandler import ModifyHandler
from aicyber.com.data_channel.Tasks import Tasks
from aicyber.com.data_channel.Task import Task

from datetime import datetime

class BaseHandler(ModifyHandler):
    tasks=Tasks()
    # def __init__(self):
    #     super(BaseHandler,self).__init__()
    #     self.tasks=Tasks()

    async def execTasks(self, tasks: list):
        print('开始执行任务。。')
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

    async def exec_postgresql_insert(self,sqls):
        res_list=[]
        if len(sqls)==0:
            return
        async with self.getToPool().acquire() as conn:
            for sql in sqls:
                print('exec sql ------->'+sql)
                res = await conn.fetch(sql)
                res = [dict(r) for r in res]
                res_list.append(res)
        return res_list

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
        # for index in res:
        #     sql='insert into {tableName}({fields}) values {values}'
        pass


    def generate_postgresql_insertsql(self, table: str, fields: list, res):
        sqls=[]
        not_insert_fields=[]
        int_insert_fields=[]
        fields_concat=''
        #遍历结果集 查找空数据以及类型转换
        for r in res:
            values=''
            for index in range(len(r)):
                cell=r[index]
                if isinstance(cell,datetime):
                    cell=cell.strftime('%Y-%m-%d %H:%M:%S')
                if cell is None:
                    not_insert_fields.append(index)
                    continue
                if isinstance(cell,int):
                    int_insert_fields.append(index)
                    cell=str(cell)
                    values+=cell+','
                    continue
                values+='\''+cell+'\''+','
            values=values[:len(values)-1]
            fields_concat=''
            #遍历字段集 去除value为空的字段
            for index in range(len(fields)):
                if index not in not_insert_fields:
                        field = fields[index]
                        fields_concat = fields_concat + '"' + field + '"' + ','
            fields_concat = fields_concat[:len(fields_concat) - 1]

            sql = 'insert into {table}({fields}) values ({values})'.format(table=table,fields=fields_concat,values=values)
            sqls.append(sql)
        return sqls



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
        from_pool = self.getFromPool()
        async with from_pool.acquire() as conn:
            async with conn.cursor() as connection:
                await connection.execute(sql)
                r = await connection.fetchall()
        return r

    async def exec_postgresql_query(self,sql):
        with self.getFromPool().acquire() as conn:
            res = conn.fetch(sql)
            res = [dict(r) for r in res]
        return await res


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

    async def select_from_mysql(self,sql):
        await self.init()
        from_pool=self.getFromPool()
        async with from_pool.acquire() as conn:
            async with conn.cursor() as connection:
                await connection.execute(sql)
                r=await connection.fetchall()
        return r

    def insert(self, sql):
        pass

    def getTableFields(self,tableName:str):
        pass

    async def default_onHandlerMethod(self):
        from_conf = self.getConf()['from']
        to_conf = self.getConf()['to']

        from_tables = from_conf.get('tables')
        to_tables = to_conf.get('tables')

        for index in from_tables:
            task = Task()
            for key in index.keys():
                value = index.get(key)
            # value为字段数组
            task.setSelectTable(key)
            task.setSelectFields(value)
            to_index = to_tables.pop(0)
            to_table_name = list(to_index.keys()).pop()
            task.setInsertTable(to_table_name)
            task.setInsertFields(to_index.get(to_table_name))
            self.tasks.addTask(task)
        print('任务指派完成。')



