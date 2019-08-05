from aicyber.com.data_channel.ModifyHandler import ModifyHandler


class BaseHandler(ModifyHandler):
    #
    # def __init__(self):
    #     super.__init__(self,ModifyHandler)




    def exec(self):
        pass


    def onHandleMethod(self):
        pass

    def select(self,sql):
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