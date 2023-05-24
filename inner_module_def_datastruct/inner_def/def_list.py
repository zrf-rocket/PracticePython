from inner_module_def_datastruct import WEIXIN_URL
my_tuple = (1, 2, 3, 4, 5)
my_set = {111, 222, 333, 444, 555}
my_dict = {'name': 'SteveRocket', 'age': 18}
my_list = [11,22,33,44,55]

# 使用list()函数将元组转换为列表
my_list1 = list(my_tuple)
print(my_list1)  # 输出：[1, 2, 3, 4, 5]

# 使用list()函数将集合转换为列表
my_list2 = list(my_set)
print(my_list2)  # 输出：[555, 333, 111, 444, 222]

# 使用list()函数将字典的键转换为列表
my_list3 = list(my_dict)
print(my_list3)  # 输出：['name', 'age']

# 使用list()转换列表，输出还是列表
print(list(my_list)) # [11, 22, 33, 44, 55]

# 使用list()转换字符串
print(list(WEIXIN_URL))