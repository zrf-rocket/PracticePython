# 1. 将整数转换为Unicode字符
print(chr(65))  # 返回值是'A'

# 2. 将十六进制数转换为Unicode字符
print(chr(0x4e2d))  # 返回值是'中'

# 3. 将Unicode编码转换为Unicode字符
print(chr(0x4e2d))  # 返回值是'中'

print(chr(0))  # 输出空格
print(chr(1000)) # 输出 Ϩ
print(chr(False)) # 输出空格

# 一些错误的用法
# print(chr(None)) # TypeError: an integer is required (got type NoneType)
# print(chr('')) # TypeError: an integer is required (got type str)
# print(chr('中文'))  # TypeError: an integer is required (got type str)
