from __init__ import WEIXIN_URL, CSDN_URL

# vars()函数的使用示例
# 返回对象的__dict__属性

class MyClass:
    def __init__(self):
        self.age = 22
        self.blog = WEIXIN_URL


obj = MyClass()
print(vars(obj))  # 输出：{'age': 22, 'blog': 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q'}

# 如果参数为空，则返回当前作用域的__dict__属性
gender = "M"
blog = CSDN_URL
print(vars())  # 输出：{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002413AB55550>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\source_code\\practice_python_1\\inner_module_def_datastruct\\inner_def\\def_vars.py', '__cached__': None, 'WEIXIN_URL': 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q', 'CSDN_URL': 'https://blog.csdn.net/zhouruifu2015/', 'MyClass': <class '__main__.MyClass'>, 'obj': <__main__.MyClass object at 0x000002413AE28650>, 'gender': 'M', 'blog': 'https://blog.csdn.net/zhouruifu2015/'}
