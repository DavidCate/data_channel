from aicyber.com.data_channel.utils.Util import Utils
from aicyber.com.data_channel.ModifyHandler import ModifyHandler
from aicyber.com.data_channel.BaseHandler import BaseHandler
import os

class Main():
    def flow(self):
       #加载用户handler
        handlers=self.loadUserHandler()
        #执行onhandle
        try:
            self.execute(handlers=handlers)
        except Exception as e:
            print(e)

    def loadUserHandler(self):
        is_handler=lambda cls:isinstance(cls,type) and issubclass(cls,BaseHandler)

    def getModules(self,package='.'):
        modules=[]
        files=os.listdir(package)
        for file in files:
            if not file.startswith('__'):
                name,ext=os.path.splitext(file)
                if ext:
                    if ext=='.py':
                        modules.append(package.replace('/','.'))





    def execute(self,handlers:list):
        pass

if __name__=='__main__':
    main=Main()
    main.flow()