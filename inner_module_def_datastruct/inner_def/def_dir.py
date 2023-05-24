# 1. 查看当前作用域内的属性和方法
print(dir())  # 输出当前作用域内的属性和方法列表
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


# 2. 查看对象的属性和方法
class MyClass:
    x = 1
    y = 2

    @classmethod
    def test1(cls):
        pass

    @staticmethod
    def test2():
        pass

    def test3(self):
        pass

obj = MyClass()
# 输出对象的属性和方法列表
print(dir(obj))  # [...... 'test1', 'test2', 'test3', 'x', 'y']


# 3. 查看模块的属性和方法
import math
print(dir(math))  # 输出模块的属性和方法列表
