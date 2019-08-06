from aicyber.com.data_channel.BaseHandler import BaseHandler
from aicyber.com.data_channel.Tasks import Tasks
from aicyber.com.data_channel.Task import Task

class MyHandler(BaseHandler):
    def onHandleMethod(self):
        task=Task()
        task.setInsertFields(['','',''])
        task.setInsertTable('cloud_call')
        task.setSelectTable('')
        task.setSelectFields(['','',''])
        self.tasks.addTask(task)
        self.execTasks()
