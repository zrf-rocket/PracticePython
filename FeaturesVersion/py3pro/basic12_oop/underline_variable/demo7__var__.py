# @author:SteveRocket 
# @Date:2023/11/19
# @File:oop1
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
from inner_module_def_datastruct import WEIXIN_URL, AGE, AUTHOR


class MyClass:
    def __init__(self, age, name, blog):
        self.age = age
        self.name = name
        self.blog = blog
        self.__age = 1
        self.__name = name
        self.__blog__ = WEIXIN_URL

    def __str__(self):
        return f"my name is {AUTHOR}"

    def __custom_method__(self):
        """前后双下划线 应用于自定义的函数"""
        return self.age

obj = MyClass(12, "steverocket", WEIXIN_URL)
print(obj)  # my name is SteveRocket
print(obj.__custom_method__())  # 12
print(obj.__custom_method__())
print(obj._MyClass__age)  # 1

print(obj._MyClass__name) # steverocket
print(obj.__blog__)  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q


# 应用于函数
# def __show__():
#     print(f"this is my {WEIXIN_URL}")
#
# __show__()  # this is my https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
