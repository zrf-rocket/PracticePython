# next()函数的使用示例
my_list = [1, 2, 3, 4, 5]

# 创建一个迭代器对象
my_iter = iter(my_list)
print(type(my_iter))
# print(len(my_iter))  #TypeError: object of type 'list_iterator' has no len()

# list(my_iter)  # 使用next前不能使用list进行操作

# 返回迭代器中的下一个元素
print(next(my_iter))  # 输出：1

# 返回迭代器中的下一个元素
print(next(my_iter))  # 输出：2

# 返回迭代器中的下一个元素，并指定默认值
print(next(my_iter, 'end'))  # 输出：3

# 返回迭代器中的下一个元素
print(next(my_iter))  # 输出：4

# 返回迭代器中的下一个元素
print(next(my_iter))  # 输出：5

# 返回迭代器中的下一个元素，并引发StopIteration异常
print(next(my_iter))  # 引发StopIteration异常
