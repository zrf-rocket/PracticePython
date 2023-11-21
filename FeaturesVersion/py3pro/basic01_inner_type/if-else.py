# @author:SteveRocket 
# @Date:2023/11/19
# @File:if-else
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
number = 10
if number % 2 == 0:
    print("number is even")  # x is even
else:
    print("number is odd")

if number % 2:
    print('number is odd')   # number is odd
else:
    print('number is even')

number = 10
result = "number is even" if number % 2 == 0 else "number is odd"
print(result)  # number is even

result = "number is odd" if number % 2 else "number is even"
print(result)  # number is even


name1, name2, name3 = "", "steverocket", "SteveRocket"
result = name1 or name2 or name3
print(result) # steverocket


var1 = 123
var2 = 123.45
var3 = "CTO Plus"
var4 = {12,3,4}
var5 = [11,22]
var6 = {"name":"SteveRocket"}
print(isinstance(var1, int))  # True
print(isinstance(var2, float))  # True
print(isinstance(var3, str))  # True
print(isinstance(var4, set))  # True
print(isinstance(var5, list))  # True
print(isinstance(var6, dict))  # True

print(type(var6) == dict) # True
print(type(var1) == int) # True

print()
print(0 == False) # True
print("" == False) # False
print(() == False) # False
print([] == False) # False
print({} == False) # False
print(None == False) # False
print(False == False) # True

if not 0:
    print("假")
if not "":
    print("假")
if not ():
    print("假")
if not []:
    print("假")
if not {}:
    print("假")
if not None:
    print("假")
if not False:
    print("假")


x = []

def y():
    print('this is fucntion y')
    return 1

a = x and y()
b = bool(x and y())

print(a, b) # [] False


username = input('please input username: ')
password = input('please input password: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'steverocket' and password == '123456':
    print('success!')
else:
    print('failed!')
