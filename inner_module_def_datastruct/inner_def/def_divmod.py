# 1. 计算整数的商和余数
result = divmod(10, 3)
print(result)  # 输出结果是(3, 1)

# 2. 计算浮点数的商和余数
result = divmod(10.5, 3.2)
print(result)  # 输出结果是(3.0, 1.0999999999999996)


# 如果参数 a 与 参数 b 都是整数，函数返回的结果相当于 (a // b, a % b)。
# 如果其中一个参数为浮点数时，函数返回的结果相当于 (q, a % b)，q 通常是 math.floor(a / b)，但也有可能是 1 ，比小，不过 q * b + a % b 的值会非常接近 a。
# 如果 a % b 的求余结果不为 0 ，则余数的正负符号跟参数 b 是一样的，若 b 是正数，余数为正数，若 b 为负数，余数也为负数，并且 0 <= abs(a % b) < abs(b)。
print(divmod(5, -2))  # (-3, -1)
print(divmod(-5, 2))  # (-3, 1)
print(divmod(-5, -2)) # (2, -1)
print(divmod(4, 2))  # (2, 0)

# 函数接收两个数字类型(非复数)参数,返回一个包含商和余数的元组(a // b, a % b)。在 python 3.x 版本该函数不支持复数。python2支持

# 3. 计算复数的商和余数
result = divmod(3+4j, 1+2j)  # TypeError: can't take floor or mod of complex number.
print(result)  # py2中输出结果是((2+0j), (1+0j))

c1 = complex(3,4)
c2 = complex(1,2)
print(c1, c2)
print(divmod(c1, c2))  # py2中输出：((2+0j), (1+0j))
