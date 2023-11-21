# 1. 判断一个值是否为真
print(bool(10))
print(bool('hello'))
print(bool([]))
print(bool(0))

# 2. 将一个值转换为布尔类型
print(bool(10))
print(bool(''))
print(bool(None))

# 3. 判断一个列表是否为空
lst = [1, 2, 3]
if lst:
    print('列表不为空')
else:
    print('列表为空')

# 4. 判断一个字典是否为空
dct = {'a': 1, 'b': 2}
if dct:
    print('字典不为空')
else:
    print('字典为空')
