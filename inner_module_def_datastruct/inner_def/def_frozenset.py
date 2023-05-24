# 1. 创建一个不可变的集合
lst = [1, 2, 3, 4, 5]
fs = frozenset(lst)
print(fs, type(fs))  # 输出结果是frozenset({1, 2, 3, 4, 5}) <class 'frozenset'>

# 2. 使用frozenset作为字典的键
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6])
d = {fs1: 'set1', fs2: 'set2'}
print(d)  # 输出结果是{frozenset({1, 2, 3}): 'set1', frozenset({4, 5, 6}): 'set2'}

# 3. 使用frozenset进行集合运算 求并集
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4])
fs3 = fs1.union(fs2)
print(fs3)  # 输出结果是frozenset({1, 2, 3, 4})
print(fs1.difference(fs2))  # fs1 不同于 fs2的元素
