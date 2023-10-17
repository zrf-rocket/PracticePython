# @author:SteveRocket 
# @Date:2023/10/17
# @File:operator_01
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

num1 = 2
num2 = 3
print(num1 ** num2)  # 8  表示2的3次方
print(4.5 ** 2)  # 计算4.5的平方  输出：20.25

import math

print(math.sqrt(16))  # 4.0

num1 = 10
num2 = 3
print(num1 + num2)  # 输出13，表示a和b的和
print(num1 - num2)  # 输出7，表示a减去b
print(num1 * num2)  # 输出30，表示a和b的乘积
print(num1 / num2)  # 输出3.3333333333333335，表示a除以b的结果（浮点数）
print(num1 // num2)  # 输出3，表示a除以b的结果（整数部分）
print(num1 % num2)  # 输出1，表示a除以b的余数

print(math.trunc(1.345))  # 1   截断为整数
print(round(1.234345, 2))  # 1.23  将数值四舍五入为2位小数，一半的数值会舍入为偶数，如果省略n，则默认为0
print(round(1.234345))  # 1
print(round(2.5))  # 2
print(math.floor(1.2))  # 1   向下取整
print(math.ceil(1.2))  # 2  向上取整



from datetime import datetime, timedelta

now = datetime.now()
yesterday = now + timedelta(days=1)
print(now, yesterday) # 2023-10-17 23:24:46.355663 2023-10-18 23:24:46.355663
print(now > yesterday) # False

print(2 < 1.5) # False
print(type(now)) # <class 'datetime.datetime'>
# print(2 < now)  # TypeError: '<' not supported between instances of 'int' and 'datetime.datetime'

t1 = (11, 22)
t2 = (11, 22)

t3, t4 = ("SteveRocket", 28), ("SteveRocket", 28)
print(t1==t2)   # True
print(t1 is t2)   # True
print(id(t1), id(t2)) # 2403642442944 2403642442944

print(t3==t4)   # True
print(t3 is t4)   # True
print(id(t3), id(t4)) # 2403642133440 2403642133440

print(11 in t1)  # True
print(11 not in t1) # False


s1 = "abcd"
s2 = "efgh"
s3 = "ABCD"
print(s1 > s2)  # False
print(s3 > s1)  # False
print(s2 > s3)  # True


num1 = 123
num2 = "456"
# print(num2 > num1)  # TypeError: '>' not supported between instances of 'str' and 'int'


print(4>3 and 4<9)  # True
print(4>3 and 4<2)  # False
print(4<3 and 4<9)  # False
print(4<3 and 4<2)  # False

# and, “与”运算， 两者都为真才是真
if True and False:
    print("is true")
else:
    print("is false") # is false

# or, "或"运算， 其中之一为真即为真
if True or False:
    print("is true")  # is true
else:
    print("is false")


# not, “非”运算， 取反
print(4 > 3)  # True
print(not 4 > 3)  # False
print(not "")  # True
print(not 4 < 3)  # True
print(not object) # False
print(not True)  # False
print(not False)  # True

x = 5
y = 10
if x > 0 and y < 20:
    print("Both conditions are true.")


x = 5
y = 25
if x > 0 or y < 20:
    print("At least one condition is true.")


x = 5
if not x > 10:
    print("Condition is not true.")