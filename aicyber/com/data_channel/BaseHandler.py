from aicyber.com.data_channel.ModifyHandler import ModifyHandler
from aicyber.com.data_channel.utils.Util import Utils

class BaseHandler(ModifyHandler):

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