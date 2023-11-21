from __init__ import WEIXIN_URL
# 对字符串进行排序
print(WEIXIN_URL)
# 输出：https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
print(''.join(sorted(WEIXIN_URL)))
# 输出：...////01678:BGHIKOPQQUWbcehiimmnoppqqqqssttwxxxy

# sorted()函数的使用示例
# 对列表进行排序
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(sorted(lst))  # 输出：[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# 对字符串列表按照长度排序
lst = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
print(sorted(lst, key=len))  # 输出：['fig', 'date', 'apple', 'banana', 'cherry', 'elderberry']

# 对字典按照值排序
dct = {'apple': 3, 'banana': 1, 'cherry': 4, 'date': 1, 'elderberry': 5, 'fig': 2}
print(sorted(dct.items(), key=lambda x: x[1]))  # 输出：[('banana', 1), ('date', 1), ('fig', 2), ('apple', 3), ('cherry', 4), ('elderberry', 5)]
