

class Tasks():
    __tasks=[]

    def addTask(self,task):
        self.__tasks.append(task)

    def getTasks(self)->list:
        return self.__tasks