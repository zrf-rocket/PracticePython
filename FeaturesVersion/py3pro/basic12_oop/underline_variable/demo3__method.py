# @author:SteveRocket 
# @Date:2023/11/19
# @File:demo3__method
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from inner_module_def_datastruct import AGE, AUTHOR, WEIXIN_URL

_MyClass__message = "this is global var"
class MyClass:
    def __init__(self):
        # 定义两个私有属性并赋值
        self._private_var = AGE
        self.__my_blog = WEIXIN_URL

    def __private_method(self):
        """
        私有方法
        :return:
        """
        print(f"this is private method, my name is {AUTHOR}")

    def public_method(self):
        """
        公有方法
        :return:
        """
        print(f"this is public method, this is my blog {WEIXIN_URL}")
        # 使用私有属性
        print(f"my age is {self._private_var}")
        # 调用私有方法
        self.__private_method()

    def mangling(self):
        return __message


MyClass().public_method()
# this is public method, this is my blog https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
# my age is 25
# this is private method, my name is SteveRocket

# MyClass().__private_method()  # AttributeError: 'MyClass' object has no attribute '__private_method'

obj = MyClass()
print(obj.mangling())  # this is global var



class OtherClass01(MyClass):
    """继承了MyClass"""
    def mangling(self):
        # return __message  # NameError: name '_OtherClass01__message' is not defined.
        return _MyClass__message

OtherClass01().mangling()

class OtherClass02:
    """未继承MyClass"""
    def mangling(self):
        # return __message  # NameError: name '_OtherClass02__message' is not defined
        return _MyClass__message

OtherClass02().mangling()