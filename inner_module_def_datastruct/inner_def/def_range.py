# range()函数的使用示例
# 生成从0开始，到5（不包含5）的整数序列
for i in range(5):
    print(i, end=' ')  # 输出：0 1 2 3 4
print()

# 生成从2开始，到5（不包含5）的整数序列
for i in range(2, 5):
    print(i, end=' ')  # 输出：2 3 4
print()

# 生成从2开始，到10（不包含10），步长为2的整数序列
for i in range(2, 10, 2):
    print(i, end=' ')  # 输出：2 4 6 8
