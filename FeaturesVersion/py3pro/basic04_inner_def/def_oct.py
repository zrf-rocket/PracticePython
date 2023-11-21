# oct()函数的使用示例
my_int = 10

# 将整数转换为八进制字符串
my_oct = oct(my_int)

# 输出八进制字符串
print(my_oct)  # 输出：0o12

# 将八进制字符串转换为整数
my_int2 = int(my_oct, 8)

# 输出转换后的整数
print(my_int2)  # 输出：10
