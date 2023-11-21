# int(x) 将x转换为一个整数。

# int()函数的使用示例
a = '123'
b = 3.14
c = True
d = '0x1F'  # 十六进制字符串

print(int(a))  # 输出：123
print(int(b))  # 输出：3
print(int(c))  # 输出：1
print(int(d, 16))  # 输出：31

# 不可以对None和空字符串使用int转换
# print(int(None))  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
print(int(''))  # ValueError: invalid literal for int() with base 10: ''
