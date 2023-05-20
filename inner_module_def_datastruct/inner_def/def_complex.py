# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

# 1. 创建一个复数对象
z = complex(3, 4)
print(z)  # 输出结果是 (3+4j)

# 2. 进行复数运算
z1 = complex(1, 2)
z2 = complex(3, 4)
z3 = z1 + z2
print(z3)  # 输出结果是(4+6j)
