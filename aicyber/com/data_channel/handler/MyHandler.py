from aicyber.com.data_channel.BaseHandler import BaseHandler
from aicyber.com.data_channel.Task import Task

class MyHandler(BaseHandler):
    async def onHandleMethod(self):
        task=Task()
        task.setInsertFields(['','',''])
        task.setInsertTable('cloud_call')
        task.setSelectTable('')
        task.setSelectFields(['','',''])
        self.tasks.addTask(task)
        await self.execTasks(self.tasks)
