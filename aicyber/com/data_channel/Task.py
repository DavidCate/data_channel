class Task():
    __selectTable = None
    __insertTable = None
    __selectFields = None
    __insertFields = None

    def setInsertTable(self, tableName:str):
        self.__insertTable=tableName

    def setInsertFields(self, fields: list):
        self.__insertFields=fields

    def setSelectFields(self, fields: list):
        self.__selectFields=fields

    def setSelectTable(self, tableName:str):
        self.__selectTable=tableName

    def getInsertTable(self):
        return self.__insertTable

    def getInsertFields(self):
        return self.__insertFields

    def getSelectTable(self):
        return self.__selectTable

    def getSelectFiles(self):
        return self.__selectFields