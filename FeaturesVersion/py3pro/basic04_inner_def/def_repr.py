# repr()函数的使用示例
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


# 创建Person对象
p = Person('SteveRocket', 18)

# 使用repr()函数输出对象的字符串形式
print(repr(p))  # 输出：Person(name=SteveRocket, age=18)
