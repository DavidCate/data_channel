

class Tasks():
    __tasks=None

    def __init__(self):
        self.__tasks=[]

    def addTask(self,task):
        self.__tasks.append(task)


    def getTasks(self)->list:
        return self.__tasks