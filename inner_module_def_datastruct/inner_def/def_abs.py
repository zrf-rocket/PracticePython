# abs() 函数返回数字的绝对值。
# 函数返回 x（数字）的绝对值，如果参数是一个复数，则返回它的大小。
num1 = -1234
num2 = abs(num1)
print(num1, num2)

# 整数
print(abs(5))  # 5
print(abs(-5))  # 5

# 浮点数
print(abs(3.14))  # 3.14
print(abs(-3.14))  # 3.14

# 复数
print(abs(3+4j))  # 5.0
print(abs(-3+4j))  # 5.0
