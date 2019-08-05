from aicyber.com.data_channel.ModifyHandler import ModifyHandler


class BaseHandler():
    __modify=None
    __conn=None
    __conf=None

    def __init__(self):
        __modify=ModifyHandler()
        __conn=__modify.getConnection()
        __conf=__modify.getConf()



    def exec(self):
        print(self.__conf)


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