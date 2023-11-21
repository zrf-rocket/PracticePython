# 1. 将方法转换为类方法
class MyClass:
    @classmethod
    def my_classmethod(cls):
        print('这是一个类方法')

MyClass.my_classmethod()  # 调用类方法

# 2. 在类方法中访问类变量
class MyClass:
    x = 0

    @classmethod
    def my_classmethod(cls):
        cls.x += 1
        print('类变量x的值为：', cls.x)

MyClass.my_classmethod()  # 调用类方法
# 类变量被修改后，直接生效
print(MyClass.x)  # 输出 1
