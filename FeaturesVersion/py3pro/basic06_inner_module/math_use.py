
from math import sin, cos, tan, asin, acos, atan, pi

# 方法1：计算三角函数
# 计算正弦值
print("sin(60) =", sin(pi / 3))

# 计算余弦值
print("cos(60) =", cos(pi / 3))

# 计算正切值
print("tan(60) =", tan(pi / 3))

print("asin =", asin(0.5))  # 返回 x 的反正弦值,结果范围在 -pi/2 到 pi/2 之间。 接收的参数为 -1 到 1
print("acos =", acos(0.5))
print("atan =", atan(pi))

# 这些函数都接收一个弧度(radian)为单位的x作为参数


# 方法2：计算指数和对数

from math import ceil, floor, pow, exp, log, sqrt

print(ceil(1.2))       # 对数值向上取整，比如x=1.2，返回2
print(floor(1.2))      # 对数值向下取整，比如x=1.2，返回1
print(pow(2,3))      # 指数运算，得到x的y次方

# 计算e的2次方
print("e的2次方 =", exp(2))

# 计算以2为底5的对数
# 对数，默认基底为e。可以使用base参数，来改变对数的基地。比如math.log(100,base=10)
print("以2为底5的对数 =", log(5, 2))
# print(log(100, base=10))  # py3.11  TypeError: log() takes no keyword arguments
print(log(100, 10))

# 2的平方根
print("2的平方根：", sqrt(2))

# 方法3： 角度和弧度互换
from math import degrees, radians
print(degrees(90))
print(radians(90))



# 方法4：两个常数
from math import pi, e

# 圆周率
print("圆周率：", pi)

# 自然对数的底
print("自然对数的底：", e)



# 方法5：双曲函数
from math import sinh, cosh, tanh, asinh, acosh, atanh
print(sinh(90))
print(cosh(90))
print(tanh(90))
print(asinh(90))
print(acosh(90))
print(atanh(0.5))



# 方法6：特殊函数
from math import erf, gamma
print(erf(90))
print(gamma(90))



# 使用内置方法 计算最大最小值

# 计算最大值
print("最大值：", max(5, 7, -4, 2))
print("最大值：", max([5, 7, -4, 2]))

# 计算最小值
print("最小值：", min(5, 7, -4, 2))
print("最小值：", min([5, 7, -4, 2]))