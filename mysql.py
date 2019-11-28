#coding=utf-8
import json
from hashlib import md5
from app.connect import ConnectDb
print '开始读取配置文件'
config = {}
sql =''
with open('./mysql.sql','r+') as f:
    sql = f.read().split(';')[:-1]  # sql文件最后一行加上;
    sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql]
connectdbobect = ConnectDb('localhost','root','zhangshuan','mysql',3306)
## 基础
def init():
    try:
        for item in sql_list:
            print item
            connectdbobect.updateDb(item)
    except ValueError as e:
        print e

if __name__ == '__main__':
    init()

