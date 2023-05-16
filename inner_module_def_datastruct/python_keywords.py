CSDN_URL = "https://blog.csdn.net/zhouruifu2015/"
WEIXIN_URL = "https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q"
GIT_URL = "https://gitee.com/SteveRocket/practice_python.git"

# 1. False：表示布尔类型的假值。
if False:
    print("https://blog.csdn.net/zhouruifu2015/")
else:
    print("https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q")


# 2. None：表示空值或缺失值。
def func():
    print("https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q")
result = func()
print(result)


# 3. True：表示布尔类型的真值。
if True:
    print("https://blog.csdn.net/zhouruifu2015/")
else:
    print("https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q")


# 4. and：逻辑与操作符。
a = 10
b = 20
if a > 5 and b < 30:
    print("https://blog.csdn.net/zhouruifu2015/")
else:
    print("https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q")

if a and b:
    print(WEIXIN_URL)
else:
    print("均为假")


# 5. as：用于给变量或模块起别名。
import numpy as np
res = np.array([11,22,33])
print(res)

try:
    1/0
except Exception as exp:
    print(exp)

# 6. assert：用于检查条件是否为真。
age = 25
assert age > 18, "age be greater than 35"
print("assert keywords1")
assert age > 35, "age be greater than 35"
print("assert keywords2")


# 7. async：用于定义异步函数。
import asyncio
async def async_def():
    print("this is python3.11")
    await asyncio.sleep(10)
    print('run over')
print('this is {}'.format(WEIXIN_URL))
asyncio.run(async_def())
print('this is {}'.format(CSDN_URL))

# 8. await：用于等待异步函数的执行结果。

# 9. break：用于跳出循环。
for i in range(10):
    if i == 5:
        break
    print(i)

# 10. class：用于定义类。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print("Hello, my name is %s, I'm %d years old, this is my blog %s" % (self.name, self.age, WEIXIN_URL))

p = Person("SteveRocket", 20)
p.say_hello()

# 11. continue：用于跳过本次循环，继续执行下一次循环。
i = 0
while 1:
    i += 1
    # 不断输出能被5整除的数
    if i % 5:
        continue
    print(i)


# 12. def：用于定义函数。
def add(a, b):
    return a + b
result = add(1, 2)
print(result)


# 13. del：用于删除对象。
lis = [1, 2, 3]
del lis[1]
print(lis)

dicts = {"name":"steverocket", 'age':22}
del dicts['age']
print(dicts)

desc = "this is my python code"
print(desc)
del desc
print(desc)


# 14. elif：用于在if语句中添加多个条件判断。
age = 25
if age > 25:
    print("age is greater than 25")
elif age < 25:
    print("age is less than 25")
else:
    print("age is equal to 25")


# 15. else：用于if语句中的否定条件。
a = 10
if a > 10:
    print("a is greater than 10")
else:
    print("a is less than or equal to 10")

# 16. except：用于捕获异常。
try:
    a = 1 / 0
except ZeroDivisionError as exp:
    print("error info：", exp)


# 17. finally：用于定义在try语句块执行完毕后必须执行的代码。
try:
    a = 1 / 0
except ZeroDivisionError:
    print("division by zero")
finally:
    print("finally block")


# 18. for：用于循环迭代。
nums = [1, 2, 3]
for i in nums:
    print(i)

lis = [i for i in range(10)]
print(lis)

# 遍历字符串
for i in WEIXIN_URL:
    print(i, end='')


# 19. from：用于从模块中导入指定的函数或变量。
from math import sqrt
print(sqrt(4))


# 20. global：用于声明全局变量。
print(WEIXIN_URL)
def func():
    global WEIXIN_URL
    WEIXIN_URL = CSDN_URL
func()
print(WEIXIN_URL)


# 21. if：用于条件判断。
age = 10
if age > 10:
    print("age is greater than 10")
elif age < 10:
    print("age is less than 10")
else:
    print("age is equal to 10")

# 22. import：用于导入模块。
import math
print(math.sqrt(4))

# 23. in：用于判断一个元素是否在一个序列中。
ages = [11, 21, 31]
if 21 in ages:
    print("21 is in age")

# 字符串是否包含另外一个字符串中
print('zhouruifu2015' in CSDN_URL)


# 24. is：用于判断两个对象是否相同。
age1 = [1, 2, 3]
age2 = age1
if age2 is age1:
    print("age2 and age1 refer to the same object")

num1 = 123
num2 = 123
print(num1 is num2) # True
print(id(num1), id(num2)) # 140707223757416 140707223757416


# 25. lambda：用于定义匿名函数。
f = lambda x: x**2
print(f(2))

lager = lambda num1,num2: num1 > num2
print(lager(22, 33))


# 26. nonlocal：用于声明外层函数中的变量。
def outer():
    x = CSDN_URL
    def inner():
        nonlocal x
        x = WEIXIN_URL
    inner()
    print(x)
outer()


# 27. not：逻辑非操作符。
if not 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q' == CSDN_URL:
    print(WEIXIN_URL)

print(not 23)  # False
print(not 0)  # True

# 28. or：逻辑或操作符。
a = 1
b = 2
if a == 1 or b == 2:
    print("either a is equal to 1 or b is equal to 2")

# 29. pass：用于占位，表示不执行任何操作。
if a > 0:
    pass
else:
    print("a is not greater than 0")


# 30. raise：用于抛出异常。
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)

# 31. return：用于从函数中返回值。
def add(num1, num2):
    return num1 + num2

result = add(11, 22)
print(result)

# 计算两个字符串的长度
result = add(len(CSDN_URL), len(WEIXIN_URL))
print(result)


# 32. try：用于捕获异常。
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print(e)

# 33. while：用于循环迭代。
i = 0
while i < 5:
    print(i)
    i += 1


# 逐个删除字符串中的字符：字符串是不可变的对象，所以先将字符串转为可变的列表
WEIXIN_URL = list(WEIXIN_URL)
while WEIXIN_URL:
    print(WEIXIN_URL.pop())


# 34. with：用于定义一个代码块的上下文环境。
with open("README.md", "r", encoding='utf-8') as f:
    content = f.read()
    print(content)

# 35. yield：用于定义生成器函数。
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in my_range(5):
    print(i)
