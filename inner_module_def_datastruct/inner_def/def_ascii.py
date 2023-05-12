# 1. 将字符串转换为ASCII字符表示：
s = "Hello, 世界"
print(ascii(s))  # 'Hello, \u4e16\u754c'

print(ascii('a'))


# 2. 将列表中的元素转换为ASCII字符表示：
lst = ["Hello", "世界"]
print([ascii(x) for x in lst])


# 3. 将字典中的值转换为ASCII字符表示：
d = {"Hello": "世界", "Python": "中文"}
print({k: ascii(v) for k, v in d.items()})


# 4. 将集合中的元素转换为ASCII字符表示：
s = {"Hello", "世界"}
print({ascii(x) for x in s})

