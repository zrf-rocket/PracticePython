# 1. 判断列表中是否存在负数
lst = [1, 2, -3, 4, 5]
print(any(x < 0 for x in lst))


# 2. 判断元组中是否存在奇数
tup = (2, 4, 6, 8, 9)
print(any(x % 2 == 1 for x in tup))


# 3. 判断集合中是否存在大写字母
s = {'a', 'B', 'c', 'd'}
print(any(x.isupper() for x in s))


# 4. 判断字典中是否存在负数：
d = {'a': 1, 'b': 2, 'c': -3, 'd': 4}
print(any(x < 0 for x in d.values()))


# 5. 判断空列表是否为True
lst = []
print(any(lst))
