# object()函数的使用示例
my_object = object()

# 输出对象的类型
print(type(my_object))  # 输出：<class 'object'>

# 检查对象是否为Python内置类型
print(isinstance(my_object, int))  # 输出：False
print(isinstance(my_object, str))  # 输出：False
print(isinstance(my_object, object))  # 输出：True


class MyObject(object):
    pass

obj = MyObject()
print(obj)  # <__main__.MyObject object at 0x7f2c5d6b0f10>
