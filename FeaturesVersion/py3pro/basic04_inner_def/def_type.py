from __init__ import WEIXIN_URL
# type()函数的使用示例

# 获取对象的类型
n = 123
print(type(n))  # 输出：<class 'int'>

print(type(WEIXIN_URL))  # 输出：<class 'str'>

lst = [1, 2, 3, 4, 5]
print(type(lst))  # 输出：<class 'list'>

# 判断对象的类型
n = 123
if type(n) == int:
    print("n is an integer")

# 类型判断  类似的参考isinstance
if isinstance(n, int):
    print("n is an integer")


# 动态创建类
MyClass = type("MyClass", (object,), {"age": 22, "my_blog": WEIXIN_URL})

obj = MyClass()
print(obj.age)  # 输出：22
print(obj.my_blog)  # 输出：https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q