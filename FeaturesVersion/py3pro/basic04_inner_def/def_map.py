# map 和 reduce 函数是什么？如何使用 map 和 reduce 函数？
# map()函数的使用示例
def square(x):
    return x ** 2

my_list = [1, 2, 3, 4, 5]

# 使用map()函数对列表中的每个元素进行平方操作
result = map(square, my_list)
print(list(result))  # 输出：[1, 4, 9, 16, 25]