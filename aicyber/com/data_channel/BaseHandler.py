from aicyber.com.data_channel.ModifyHandler import ModifyHandler


class BaseHandler(ModifyHandler):
    __selectTable=None
    __insertTable=None
    __selectFields=None
    __InsertFields=None



    def exec(self):
        pass


    def onHandleMethod(self):
        pass

    async def select(self,sql):
        pass

    def insert(self,sql):
        pass

    def setInsertTable(self,table):
        pass

    def setInsertFields(self,fields:list):
        pass

    def setSelectFields(self,fields:list):
        pass

    def setSelectTable(self,table):
        pass