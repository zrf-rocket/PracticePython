# 1. 获取对象的属性值
class Person:
    name = 'steverocket'
    age = 20

p = Person()
name = getattr(p, 'name')
age = getattr(p, 'age')
print(name, age)  # 输出结果是steverocket 20

# 2. 如果属性不存在则返回默认值
from inner_module_def_datastruct import WEIXIN_URL
class Person:
    name = 'steverocket'
    age = 20

p = Person()
gender = getattr(p, 'gender', 'unknown')
blog = getattr(p, 'blog', WEIXIN_URL)
print(gender)  # 输出结果是unknown
print(blog) # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

# 3. 获取模块的属性值
import math
pi = getattr(math, 'pi')
print(pi)  # 输出结果是3.141592653589793
