from aicyber.com.data_channel.BaseHandler import BaseHandler
from aicyber.com.data_channel.Tasks import Tasks
from aicyber.com.data_channel.Task import Task

class MyHandler(BaseHandler):
    async def onHandleMethod(self):
        task=Task()
        from_conf=self.getConf()['from']
        to_conf=self.getConf()['to']

        from_tables=from_conf.get('tables')
        to_tables=to_conf.get('tables')

        xx=dict({"cloud_app":['id','addtime']})
        for key in xx.keys():
            value=xx.get(key)

        for index in from_tables:
            for key in index.keys():
                value=index.get(key)
            task.setSelectTable(index)
            # task.setSelectFields()
            # task.setInsertTable(to_tables.pop(index=0))
            # task.setInsertFields()
            # self.tasks.addTask(task)

        sql = 'select * from cloud_line'

        res=await self.select(sql)
        print(res)
        await self.execTasks(self.tasks)
