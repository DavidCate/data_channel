from aicyber.com.data_channel.BaseHandler import BaseHandler
from aicyber.com.data_channel.Task import Task

class MyHandler(BaseHandler):
    async def onHandleMethod(self):
        # task=Task()
        # from_conf=self.getConf()['from']
        # to_conf=self.getConf()['to']
        #
        # from_tables=from_conf.get('tables')
        # to_tables=to_conf.get('tables')
        #
        # xx=dict({"cloud_app":['id','addtime']})
        # for key in xx.keys():
        #     value=xx.get(key)
        #
        # for index in from_tables:
        #     for key in index.keys():
        #         value=index.get(key)
        #     task.setSelectTable(index)
        #     task.setSelectFields('id','name','age')
        #     task.setInsertTable(to_tables.pop(index=0))
        #     task.setInsertFields('id','name','age')
        #     self.tasks.addTask(task)
        #
        # await self.execTasks(self.tasks)
        sql='select * from student'
        await self.init()
        pool=self.getFromPool()
        async with pool.acquire() as connection:
            async with connection.cursor() as connection:
                await connection.execute("select * from student")
                data = connection.fetchall()
                print(data)

