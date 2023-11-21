# @author:SteveRocket 
# @Date:2023/11/21
# @File:str-format
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
from inner_module_def_datastruct import AGE, AUTHOR, WEIXIN_URL

print(f"My name is {AUTHOR}, and I am {AGE} years old. this is my blog {WEIXIN_URL}")


# My name is SteveRocket, and I am 25 years old. this is my blog https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

def show():
    print("函数被调用")
    return AUTHOR


print(f"{show()}:{11 + 22}")  # SteveRocket:33

message = "{0} {name}".format(WEIXIN_URL, name=AUTHOR)
print(message)  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q SteveRocket
message = "{0} {0} {name} {name}".format(WEIXIN_URL, name=AUTHOR)
print(message)  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q SteveRocket SteveRocket

num1, num2 = 11, 22
print("%s %d + %d = %d" % ("计算两数的和：", num1, num2, num1 + num2))  # 计算两数的和： 11 + 22 = 33

print("my name is: %(name)s  age is: %(age)d" % {"name": AUTHOR, "age": AGE})  # my name is: SteveRocket  age is: 25

print("%+10x" % 10)  #         +a
print("%04d" % 5)  # 0005
print("%6.3f" % 2.3)  #  2.300
print("%.*f" % (4, 1.2)) # 1.2000

# 不设置指定位置，按默认顺序
print("{} {}".format(AUTHOR, AGE)) # SteveRocket 25
# 设置指定位置
print("{0} {1}".format(AUTHOR, AGE)) # SteveRocket 25
# 设置指定位置
print("{1} {0}".format(AUTHOR, AGE)) # 25 SteveRocket

print('计算两数的和：{0} * {1} = {2}'.format(num1, num2, num1 + num2))  # 计算两数的和：11 * 22 = 33

print("my name is: {name}  age is: {age}".format(name=AUTHOR, age = AGE)) # my name is: SteveRocket  age is: 25

information = {"name": AUTHOR, "age":AGE, "platform":"微信公众号：CTO Plus"}
print("name name is {name} age is {age} {platform}".format(**information)) # name name is SteveRocket age is 25 微信公众号：CTO Plus

informations = [AUTHOR, AGE, "微信公众号：CTO Plus"]  # 这里如果是set则会报错
print("{0[0]}  {0[1]}  {0[2]}".format(informations))  # SteveRocket  25  微信公众号：CTO Plus

print(f'计算两数的和：{num1} * {num2} = {num1 + num2}')  # 计算两数的和：11 * 22 = 33


def func(tpl: str, param1: str, param2: str) -> str:
    return tpl.format(param1=param1, param2=param2)

some_template = "First template: {param1}, {param2}"
another_template = "Other template: {param1} and {param2}"
print(func(some_template, "Hello", "CTO Plus"))  # First template: Hello, CTO Plus
print(func(another_template, "Hello", "SteveRocket"))  # Other template: Hello and SteveRocket

# 动态重用具有不同参数的相同模板.
inputs = ["公众号：CTO Plus", "SteveRocket", 25]
template = "Here's some dynamic value: {value}"

for value in inputs:
    print(template.format(value=value))
# Here's some dynamic value: 公众号：CTO Plus
# Here's some dynamic value: SteveRocket
# Here's some dynamic value: 25


data_id = 1234
# 不好的使用建议
metric_name = '%s_clsuter_id' % data_id

# 好的使用建议
metric_name = '{}_cluster_id'.format(data_id)

# 更好的使用建议
metric_name = f'{data_id}_cluster_id'

# 当需要重复键入格式化变量名时，使用 f-strings。

a, b, c, d =  11,22,33,44
# 不推荐
"{a}-{b}-{c}-{d}".format(a=a, b=b, c=c, d=d)

# 推荐
f"{a}-{b}-{c}-{d}"
