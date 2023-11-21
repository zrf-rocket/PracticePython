# 将整数转换为二进制字符串
print(bin(10))
# bin('10')  # TypeError: 'str' object cannot be interpreted as an integer
# bin(010)  # SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers


# 2. 将二进制字符串转换为整数
print(int('0b1010', 2))
print(int('0b10100', 2))


# 3. 将整数转换为八进制字符串
print(type(oct(10)), oct(10))
print(type(oct(20)), oct(20))

# 4. 将整数转换为十六进制字符串
print(type(hex(10)), hex(10))
print(type(hex(20)), hex(20))
