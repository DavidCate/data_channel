from aicyber.com.data_channel.utils.Util import Utils

class ModifyHandler():
    __datasourceConnection=None
    __targetdatasourceConnection=None

    def __init__(self):
        util=Utils()
        conf=util.getConf()
        self.initConnection(self,conf)

    def getDataSourceTables(self):
        pass

    def getTargetDataSourceTables(self):
        pass

    def initConnection(self,conf):
        pass

