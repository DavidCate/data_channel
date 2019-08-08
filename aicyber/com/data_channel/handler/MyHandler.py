from aicyber.com.data_channel.BaseHandler import BaseHandler
from aicyber.com.data_channel.Tasks import Tasks
from aicyber.com.data_channel.Task import Task

import json

class MyHandler(BaseHandler):
    async def onHandleMethod(self):
        await self.default_onHandlerMethod()
        # sql = 'select * from cloud_line'
        # sql='select * from line'
        # res=await self.select_from_mysql(sql)

        # res=await self.select(sql)
        # print(res)
        await self.execTasks(self.tasks)
