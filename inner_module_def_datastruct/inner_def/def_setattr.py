from __init__ import WEIXIN_URL


# setattr()函数的使用示例
class Person:
    pass


# 创建Person对象
p = Person()

# 设置对象属性
setattr(p, 'name', 'SteveRocket')
setattr(p, 'age', 24)
setattr(p, 'blog', WEIXIN_URL)

# 输出对象属性值
print(getattr(p, 'name'))  # 输出：SteveRocket
print(getattr(p, 'age'))  # 输出：24
print(p.blog) # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
# print(p.gender) # AttributeError: 'Person' object has no attribute 'gender'