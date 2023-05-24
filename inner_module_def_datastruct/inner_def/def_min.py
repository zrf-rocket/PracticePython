from inner_module_def_datastruct import WEIXIN_URL
# min()函数的使用示例
my_list = [1, 3, 5, 7, 9]

# 返回列表中的最小值
print(min(my_list))     # 输出：1

my_str = 'python'

# 返回字符串中的最小字符
print(min(my_str))      # 输出：h
print(min(WEIXIN_URL))  # 输出：.

my_dict = {'name': 'steverocket', 'age': 18}

# 返回字典中的最小键
print(min(my_dict))  # 输出：age

t1 = (WEIXIN_URL)
print(min(t1))      # 输出：.
# s1 = {1, 6, 3, 9, 3, 7, ""}   # TypeError: '<' not supported between instances of 'str' and 'int'
# s1 = {1, 6, 3, 9, 3, 7, 'a'}   # TypeError: '<' not supported between instances of 'str' and 'int'
s1 = {1, 6, 3, 9, 3, 7}
print(min(s1))      # 1


# min()函数的key参数示例
my_list = ['apple', 'banana', 'orange', 'watermelon']

# 返回列表中长度最短的元素
print(min(my_list, key=len))  # 输出：apple
