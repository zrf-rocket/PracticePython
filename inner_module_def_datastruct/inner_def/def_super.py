from __init__ import WEIXIN_URL
# super()函数的使用示例

# 定义父类
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, %s!" % self.name)


# 定义子类
class Student(Person):
    def __init__(self, name, blog):
        super().__init__(name)  # 调用父类的构造方法
        self.blog = blog

    def say_hello(self):
        super().say_hello()  # 调用父类的方法
        print("this is my blog %s" % self.blog)


# 创建对象并调用方法
s = Student("SteveRocket", WEIXIN_URL)
s.say_hello()
# 输出：Hello, SteveRocket!
# this is my blog https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
