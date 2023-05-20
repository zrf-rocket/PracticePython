# help() 函数用于查看函数或模块用途的详细说明。
help('sys') # 查看 sys 模块的帮助

# help()函数的使用示例
# 获取模块帮助信息
import math
help(math)

# 获取函数帮助信息
def add(a, b):
    """
    This function adds two numbers.
    """
    return a + b

help(add)

# 获取类帮助信息
class Person:
    """
    This is a Person class.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        """
        This method prints a greeting message.
        """
        print("Hello, my name is", self.name)

help(Person)

# 获取对象帮助信息
person = Person("Alice", 18)
help(person)

# 进入交互式帮助模式
# help()
# 输入对象名称，如math、add、Person、person等，即可获取帮助信息
