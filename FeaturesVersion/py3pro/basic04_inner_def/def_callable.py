from inner_module_def_datastruct import WEIXIN_URL

# 1. 判断函数是否可调用
def func():
    pass

if callable(func):
    print('函数是可调用的')
else:
    print('函数不可调用')

# 2. 判断类是否可调用
class MyClass:
    pass

if callable(MyClass):
    print('类是可调用的')
else:
    print('类不可调用')

# 3. 判断实例对象是否可调用
class MyClass:
    def __call__(self):
        pass

obj = MyClass()

if callable(obj):
    print('实例对象是可调用的')
else:
    print('实例对象不可调用')

# 4. 整个字符串 判断是否可调用
print(callable(WEIXIN_URL))

