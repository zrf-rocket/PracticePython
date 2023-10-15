# set()函数的使用示例
# 创建集合
s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])

# 集合运算
# s1和s2的并集
print(s1.union(s2))  # 输出：{1, 2, 3, 4, 5, 6, 7}

# s1与s2的交集
print(s1.intersection(s2))  # 输出：{3, 4, 5}

# s1不同于s2的元素
print(s1.difference(s2))  # 输出：{1, 2}


from inner_module_def_datastruct import WEIXIN_URL

a = [1, 2.2, WEIXIN_URL]
b = [WEIXIN_URL, False]
print(set(a).union(set(b)))
