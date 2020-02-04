'''读取数据文件'''

'''读取txt文件'''
'''read():读取整个文件'''
'''readline():读取一行数据'''
'''readlines():读取所有行的数据'''

# 读取文件
with(open("D:\\testdata\\test1.txt","r")) as txt_file:
    data = txt_file.readlines()
#格式化处理
users = []
for line in data:
    user = line[:-1].split(":")
    users.append(user)
#打印users二二维数组
print(users)

'''读取csv文件'''
import csv
import codecs
from itertools import islice

'''读取本地csv文件'''
data = csv.reader(codecs.open("D:\\testdata\\test2.csv","r","utf-8","ignore"))
#存放用户数据
users = []
#循环输出每行信息
for line in islice(data,1,None):
    users.append(line)
#打印
print(users)
print(len(users))

'''读取xml文件'''
'''略'''

'''读取json文件'''
import json

with open("D:\\testdata\\test4.json","r") as f:
    data = f.read()
user_list = json.loads(data)
print(user_list)

for up in user_list:
    print(up["username"])
    print(up["password"])






