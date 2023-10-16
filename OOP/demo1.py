# @author:SteveRocket 
# @Date:2023/7/4
# @File:demo1
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name)

if __name__ == '__main__':
    p = Person('SteveRocket', 25)
    p.say_hello()  # Hello, my name is SteveRocket