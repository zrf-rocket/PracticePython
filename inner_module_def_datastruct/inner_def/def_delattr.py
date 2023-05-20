# 1. 删除对象的属性
class MyClass:
    x = 1
    y = 2

obj = MyClass()
print(obj.x, obj.y)  # 输出结果是1, 2
delattr(obj, 'x')  # 删除属性x
print(obj.y)  # 输出结果是2

# 2. 删除对象的不存在的属性
class MyClass:
    x = 1
    y = 2

obj = MyClass()
delattr(obj, 'z')  # 删除不存在的属性z，会抛出AttributeError异常
