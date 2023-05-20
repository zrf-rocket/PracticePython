class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)

person = Person("SteveRocket")

# 判断对象是否具有指定属性或方法
print(hasattr(person, "name"))  # True
print(hasattr(person, "age"))  # False
print(hasattr(person, "say_hello"))  # True
print(hasattr(person, "walk"))  # False

# 判断对象是否具有指定属性或方法，并执行相应操作
if hasattr(person, "say_hello"):
    person.say_hello()  # Hello, my name is SteveRocket
else:
    print("Object has no attribute 'say_hello'")

# 判断对象是否为None
obj = None
print(hasattr(obj, "name"))  # False

# 参数错误示例
# print(hasattr(person, 123))  # TypeError: hasattr(): attribute name must be string

