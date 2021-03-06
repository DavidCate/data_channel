from aicyber.com.data_channel.BaseHandler import BaseHandler
import os
import importlib
import asyncio

class Main():
    async def flow(self):
       #加载用户handler
        handlers=self.loadUserHandler()
        #执行onhandle
        try:
            await self.execute(handlers=handlers)
        except Exception as e:
            print(e)

    def loadUserHandler(self,package='./handler'):
        is_handler = lambda cls: isinstance(cls, type) and issubclass(cls, BaseHandler)
        modules = []
        handlers=[]
        def get_file(package):
            files = os.listdir(package)
            for file in files:
                if not file.startswith("__"):
                    name, ext = os.path.splitext(file)
                    if ext:
                        if ext == '.py':
                            modules.append(package.replace('/', '.') + "." + name)
                    else:
                        # 文件夹
                        get_file(package + "/" + name)
        get_file(package)
        for module in modules:
            module = importlib.import_module(module, package)
            #遍历模块中的属性
            for i in dir(module):
                if i.endswith('Handler') and not i.startswith('Base'):
                    cls=getattr(module,i)
                    if is_handler(cls):
                        cls = cls()
                        handlers.append(cls)
        return handlers


    async def execute(self,handlers:list):
        for handler in handlers:
            #处理用户的操作 对用户的操作进行配置
            await handler.onHandleMethod()
            #根据配置好的配置，执行父类查询和插入
            ##########


if __name__=='__main__':
    event_loop=asyncio.get_event_loop()
    event_loop.run_until_complete(Main().flow())
