from inner_module_def_datastruct import WEIXIN_URL
# 1. 过滤列表中的偶数
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0, lst)
print(list(result))  # 输出结果是[2, 4, 6, 8]

# 2. 过滤字符串中的元音字母
s = WEIXIN_URL
result = filter(lambda x: x not in ['a', 'e', 'i', 'o', 'u'], s)
print(''.join(result))  # 输出结果是'https://mp.wxn.qq.cm/s/0yqGBPbOI6QxHqK17WxU8Q'

# 3. 过滤元组中的负数
t = (1, -2, 3, -4, 5, -6)
result = filter(lambda x: x >= 0, t)
print(tuple(result))  # 输出结果是(1, 3, 5)
