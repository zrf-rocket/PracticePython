# property()函数的使用示例
class Person:
    def __init__(self, name):
        self._name = name

    # getter方法
    @property
    def name(self):
        return self._name

    # setter方法
    @name.setter
    def name(self, value):
        self._name = value

    # deleter方法
    @name.deleter
    def name(self):
        del self._name


# 创建Person对象
p = Person('SteveRocket')

# 获取name属性
print(p.name)  # 输出：SteveRocket

# 设置name属性
p.name = 'SteveRocket02'
print(p.name)  # 输出：SteveRocket02

# 删除name属性
del p.name
print(p.name)  # 报错：AttributeError: 'Person' object has no attribute '_name'
