# @author:SteveRocket 
# @Date:2023/11/18
# @File:demo4_var_method
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
from inner_module_def_datastruct import AGE, AUTHOR

class MyClass:
    """
    单下划线在变量和方法中的使用示例
    """
    _author = AUTHOR
    age = AGE

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

demo_obj = MyClass()
print(demo_obj.calculate_average([1, 2, 3, 4]))  # 2.5
print(demo_obj._show_msg())  # SteveRocket
print(demo_obj._author)  # SteveRocket
print(demo_obj.age)  # 25
print(demo_obj.user)  # steverocket
print(demo_obj._blog) # 公众号：CTO Plus
