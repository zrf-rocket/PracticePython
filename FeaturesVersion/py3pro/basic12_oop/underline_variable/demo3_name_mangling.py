# @author:SteveRocket 
# @Date:2023/11/18
# @File:demo3_name_mangling
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
from inner_module_def_datastruct import AGE, AUTHOR, WEIXIN_URL


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


obj = MyClass()
obj.public_method()
# this is public method, this is my blog https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
# my age is 25
# this is private method, my name is SteveRocket

obj._MyClass__private_method()  # 通过名称修饰访问私有方法
# this is private method, my name is SteveRocket

# print(obj._MyClass_private_var)  # AttributeError: 'MyClass' object has no attribute '_MyClass_private_var'
# print(obj._MyClass__private_var) # AttributeError: 'MyClass' object has no attribute '_MyClass__private_var'

# 通过名称修饰访问私有属性
print(obj._MyClass__my_blog)  # 输出 https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q


class MyClass02:
    def __init__(self):
        self.age = AGE
        self._author = AUTHOR
        self.__blog = WEIXIN_URL

obj = MyClass02()
print(dir(obj))

class SubMyClass02(MyClass02):
    """
    集成自MyClass02
    """
    def __init__(self):
        super().__init__()
        self.age = 0
        self._author = 'steverocket'
        self.__blog = 'cto plus'

sub_obj = SubMyClass02()
print(dir(sub_obj))
print(sub_obj.age)   # 0
print(sub_obj._author) # steverocket

# print(sub_obj._SubMyClass02_author)  # AttributeError: 'SubMyClass02' object has no attribute
print(sub_obj._SubMyClass02__blog) # cto plus
# # print(sub_obj.__blog) # AttributeError: 'SubMyClass02' object has no attribute '__blog'