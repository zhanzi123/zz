# a = input("请输入号码")
# if str(a) in str(7):
#     print("caonima")
# n = 0
# for i in range(0,100000):
#     if  str(7) in str(i):
#         n = n + 1
# print(n)

# x = 0
# for i in range(0,100000):
#     if  str(77777) in str(i):
#         x = x + 1999
#     elif str(7777) in str(i):
#         x = x + 599
#     elif str(777) in str(i):
#         x = x + 199
#     elif str(77) in str(i):
#         x = x + 98
#     elif str(7) in str(i):
#         x = x + 1
#     else:
#         pass
# print(x)
import pytest
#假设次功能的代码方法为zhongjiang
def zhongjiang(m):
    pass
for i in range(0,100000):
    if  str(77777) in str(i):
        x =  1999
    elif str(7777) in str(i):
        x =  599
    elif str(777) in str(i):
        x =  199
    elif str(77) in str(i):
        x =  98
    elif str(7) in str(i):
        x =  1
    else:
        x = 0
    if x == zhongjiang(i):
        pass
    else:
        print("数字为"+i+"时程序计算错误")




