# @author:SteveRocket 
# @Date:2023/5/14
# @File:def_max
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/


# max()函数的使用示例
my_list = [1, 3, 5, 7, 9]

# 返回列表中的最大值
print(max(my_list))  # 输出：9

# 返回列表中的最大字符串值
infos = ["https", "zhouruifu2015", "blog.csdn.net"]
print(max(infos))  # zhouruifu2015

my_str = 'SteveRocket Python3.11'

# 返回字符串中的最大字符
print(max(my_str))  # 输出：y

my_dict = {'name': 'Tom', 'age': 18}
my_dict2 = {123: 'steverocket', 456: 'rocket'}

# 返回字典中的最大键
print(max(my_dict))  # 输出：name
print(max(my_dict2))  # 输出：456


# max()函数的key参数示例
my_list = ['apple', 'banana', 'orange', 'watermelon']

# 返回列表中长度最长的元素
print(max(my_list, key=len))  # 输出：watermelon

# 如果列表里面存在两个相同长度的字符串 则返回列表中第一个出现的元素
print(max(infos, key=len))  # blog.csdn.net
