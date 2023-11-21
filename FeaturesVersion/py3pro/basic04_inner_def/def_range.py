# range()函数的使用示例
print(list(range(-9)))  # []
print(list(range(0, -9)))  # []
print(list(range(0)))  # []
print(list(range(0, -9, -1)))  # [0, -1, -2, -3, -4, -5, -6, -7, -8]
# 输出0到10之间的偶数
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]


elements = ["I", "am", "steverocket"]
for index, element in enumerate(elements):
    print(index, element)

for i in range(len(elements)):
    print(i, elements[i])


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
