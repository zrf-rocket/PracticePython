# @author:SteveRocket 
# @Date:2023/11/13
# @File:下划线的作用
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

class DemoObj:
    _age01 = 123
    age02 = 456

    def __init__(self):
        self.user = 'steverocket'
        self._blog = '公众号：CTO Plus'
    def calculate_average(self, numbers):
        _sum = sum(numbers)
        _count = len(numbers)
        _average = _sum / _count
        return _average

    def _show_msg(self, author="SteveRocket"):
        return author

# demo_obj = DemoObj()
# print(demo_obj.calculate_average([1, 2, 3, 4]))  # 2.5
# print(demo_obj._show_msg())  # SteveRocket
# print(demo_obj._age01)  # 123
# print(demo_obj.age02)  # 456
# print(demo_obj.user)  # steverocket
# print(demo_obj._blog) # 公众号：CTO Plus


from pkg01.module01 import *
# 直接调用函数
function("module01")   # this is function module01
# 直接使用变量
print(my_blog)  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
# 直接使用类
obj = DemoClass()
obj.show("this is module01")  # this is module01

# 使用通配符导入，下面带有前缀下划线的变量全都不能被导入使用
# print(__author__) # NameError: name '__author__' is not defined
# print(_age)  # NameError: name '_age' is not defined. Did you mean: 'range'?

from pkg01.module02 import *
# 使用通配符导入，下面的module02中的方法全都不能被导入使用
# _function()  # NameError: name '_function' is not defined. Did you mean: 'function'?
# __function()
# __function__()


from pkg01 import module02
# 不使用通配符的方式导入，则还可以使用
module02._function()  # this is _function
module02.__function() # this is __function
module02.__function__() # this is __function__
