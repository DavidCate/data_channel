import yaml
import os

class Utils():
    __yamlName='config.yaml'

    __conf={}

    def __init__(self):
        self.setConf()
        self.verifyDataSource()


    def getYamlPath(self):
        filePath=os.path.realpath(__file__)
        fileNamePath=os.path.split(filePath)[0]
        confDir=os.path.join(fileNamePath,'../conf')
        yamlPath=os.path.join(confDir,self.__yamlName)
        print(yamlPath)
        return yamlPath

    def setConf(self):
        try:
            with open(self.getYamlPath(),'r',encoding='utf-8') as f:
                self.__conf=yaml.load(f.read(),Loader=yaml.FullLoader)
        except Exception as e:
            print(e)

    def getConf(self):
        if self.__conf is not None:
            return self.__conf
        else:
            print('配置文件读取失败')
            return None

    def verifyDataSource(self):
        conf=self.__conf
        if conf.get('from') is not None and conf.get('to') is not None:
            datasource=conf['from']
            target=conf['to']
            d_dbtype=datasource.get('db_type')
            d_host=datasource.get('host')
            d_port=datasource.get('port')
            d_user=datasource.get('user')
            d_pwd=datasource.get('pwd')
            d_database=datasource.get('database')
            d_tables=datasource.get('tables')
            t_dbtype=target.get('db_type')
            t_host=target.get('host')
            t_port=target.get('port')
            t_user=target.get('user')
            t_pwd=target.get('pwd')
            t_database=target.get('database')
            t_tables=target.get('tables')
            if d_database is None:
                raise Exception('数据源未指定数据库')
            if d_dbtype is None:
                raise Exception('数据源未指定数据库类型')
            if d_host is None:
                raise Exception('数据源未指定host')
            if d_port is None:
                raise Exception('数据源未指定port')
            if d_pwd is None:
                raise Exception('数据源未指定密码')
            if d_user is None:
                raise Exception('数据源未指定用户名')
            if len(d_tables)<=0:
                raise Exception('数据源未指定导出的数据表')
            if t_database is None:
                raise Exception('目标数据源未指定数据库')
            if t_dbtype is None:
                raise Exception('目标数据源未指定数据库类型')
            if t_host is None:
                raise Exception('目标数据源未指定host')
            if t_port is None:
                raise Exception('目标数据源未指定port')
            if t_pwd is None:
                raise Exception('目标数据源未指定密码')
            if t_user is None:
                raise Exception('目标数据源未指定用户名')
            if len(t_tables)<=0:
                raise Exception('目标数据源未指定导出的数据表')
        else:
            raise Exception('配置文件错误，缺少输入源或输出源')


if __name__=='__main__':
    util=Utils()
    conf=util.getConf()

