# iter()函数的使用示例
my_list = [1, 2, 3, 4, 5]
my_dict = {'name': 'SteveRocket', 'age': 18}

# 使用iter()函数获取列表的迭代器
my_list_iterator = iter(my_list)
print(type(my_list_iterator))  # <class 'list_iterator'>

# 使用next()函数遍历列表
print(next(my_list_iterator))  # 输出：1
print(next(my_list_iterator))  # 输出：2

# 使用iter()函数获取字典的迭代器
my_dict_iterator = iter(my_dict)
print(type(my_dict_iterator))  # <class 'dict_keyiterator'>

# 使用next()函数遍历字典
print(next(my_dict_iterator))  # 输出：'name'
print(next(my_dict_iterator))  # 输出：'age'

# 如果没有值可以继续next，则抛出 StopIteration 异常
# print(next(my_dict_iterator))  # StopIteration

# 如果没有值可以继续next，通过指定第二个参数来作为指定默认输出，则不会报错
print(next(my_dict_iterator, "Not Exists"))  # 输出 Not Exists
