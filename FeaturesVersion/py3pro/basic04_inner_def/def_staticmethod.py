from __init__ import WEIXIN_URL
# staticmethod()函数的使用示例

class MyClass:
    x = 0
    def __init__(self, y):
        self.y = y

    @staticmethod
    def my_static_method():
        print("This is a static method.", WEIXIN_URL)

# 调用静态方法
MyClass.my_static_method()  # 输出：This is a static method. https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

# 创建实例并调用静态方法
obj = MyClass(1)
obj.my_static_method()  # 输出：This is a static method. https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q