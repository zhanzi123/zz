from pymysql import connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
#读取db——config.ini文件
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + "/db_config.ini"

cf =cparser.ConfigParser
cf.read(file_path)
host = cf.get("mysqlconf","host")
port = cf.get("mysqlconf","port")
db = cf.get("mysqlconf","db")
user = cf.get("mysqlconf","user")
password = cf.get("mysqlconf","password")
# 封装mysql基本操作
class DB:
    def __init__(self):
        try:
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print("mysql error %d:%s"%(e.args[0],e.args[1]))
    # 清楚表数据
    def clear(self,table_name):
        real_sql = "delete from" + table_name +";"
        # real_sql = "truncate table" + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()
    # 插入表数据
    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
            key = ','.join(table_data.keys())
            value = ','.join(table_data.values())
            real_sql = "insert into"+table_name+"("+key+")values("+values+")"
            with self.conn.cursor() as cursor:
                cursor.execute(real_sql)
            self.conn.commit()
    # 关闭数据库连接
    def close(self):
        self.conn.close()

if __name__ == '__main__':
    db = DB()
    table_name = "sign_event"
    data = {'id':12,'name':'红米','limit':2000,'status':1,'address':'北京会展中心','start_tme':'2016-08-20 00:25:42'}
    db.clear(table_name)
    db.insert(table_name,data)
    db.close()