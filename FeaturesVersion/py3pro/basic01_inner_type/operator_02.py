# @author:SteveRocket 
# @Date:2023/10/17
# @File:operator_02
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from FeaturesVersion import AGE, AUTHOR, BLOG, WEIXIN_URL
# user_infos = [AGE, AUTHOR, BLOG, WEIXIN_URL]
# print(user_infos)  # [28, 'steverocket', '微信公众号：CTO Plus', 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q']
# print(28 in user_infos) # True
# print("Cramer" not in user_infos) # True



num1 = 123
num2 = 123
num3 = int("123")
print(num1 == num2) # True
print(num1 is num2, num1 is num3) # True True
print(id(num1), id(num2), id(num3)) # 140735343489640 140735343489640 140735343489640

li1 = [11,22]
li2 = [11,22]
print(li1 == li2)  # True
print(li1 is li2)  # False
print(id(li1), id(li2))  # 2972199640896 2972203093504



value1, value2, value3 = 11, 22, 33
print(value1, value2, value3)  # 11 22 33

value1, value2, value3 = AGE, AUTHOR, [WEIXIN_URL, BLOG]
print(value1, value2, value3) # 28 steverocket ['https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q', '微信公众号：CTO Plus']

value = AGE, AUTHOR, [WEIXIN_URL, BLOG]
print(type(value), value)  # <class 'tuple'> (28, 'steverocket', ['https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q', '微信公众号：CTO Plus'])

print(value1, value2)  # 28 steverocket

value1, value2 = value2, value1
print(value1, value2)  # steverocket 28


value1 = value2 = value3 = AGE
print(value1, value2, value3)  # 28 28 28
print(id(value1), id(value2), id(value3))  # 140735345649288 140735345649288 140735345649288
print(value1 is value3)  # True


name = "SteveRocket"

alias, age, blog = name, 25, "https://blog.csdn.net/zhouruifu2015/"
print(id(alias) == id(name))  # True
print(alias, age, blog)  # SteveRocket 25 https://blog.csdn.net/zhouruifu2015/

infos = name, 25, "https://blog.csdn.net/zhouruifu2015/"
print(infos)  # ('SteveRocket', 25, 'https://blog.csdn.net/zhouruifu2015/')
