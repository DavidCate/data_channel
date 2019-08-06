class Sqls():
    __selectSQL=None
    __insertSQL=None

    def setSelectSQL(self,sql):
        self.__selectSQL=sql

    def setInsertSQL(self,sql):
        self.__insertSQL=sql

    def getSelectSQL(self):
        return self.__selectSQL

    def getInsertSQL(self):
        return self.__insertSQL