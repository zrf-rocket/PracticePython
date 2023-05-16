# sum()函数的使用示例
# 对整数序列求和
nums = [1, 2, 3, 4, 5]
print(sum(nums))  # 输出：15


# 对浮点数序列求和
nums = [1.0, 2.0, 3.0, 4.0, 5.0]
print(sum(nums))  # 输出：15.0


# 对字符串序列求和
words = ["hello", "world"]
# print(sum(words))  # 报错：TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 对字符串求和
from __init__ import WEIXIN_URL
# print(sum(WEIXIN_URL)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'


# 指定求和的起始值
nums = [1, 2, 3, 4, 5]
print(sum(nums, 10))  # 输出：25


# 指定求和的数据类型
nums = [1, 2, 3, 4, 5]
print(sum(nums, 0.0))  # 输出：15.0