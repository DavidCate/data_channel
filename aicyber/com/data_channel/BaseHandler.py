from aicyber.com.data_channel.ModifyHandler import ModifyHandler
from aicyber.com.data_channel.Tasks import Tasks
from aicyber.com.data_channel.Task import Task
from typing import TypeVar,Generic

class BaseHandler(ModifyHandler):
    tasks=Tasks()

    def execTasks(self,tasks:Tasks):
        tasks=tasks.getTasks()
        for task in tasks:
            self.execTask(task)

    def execTask(self,task:Task):
        sqls=self.generate_sqls_by_task(task)



    def onHandleMethod(self):
        pass

    async def select(self,sql):
        pass

    def insert(self,sql):
        pass

