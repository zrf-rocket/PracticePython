from __init__ import WEIXIN_URL
# tuple()函数的使用示例

# 将列表转换为元组
lst = [1, 2, 3, 4, 5]
tpl = tuple(lst)
print(tpl)  # 输出：(1, 2, 3, 4, 5)

# 将字符串转换为元组
print(WEIXIN_URL)  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
tpl2 = tuple(WEIXIN_URL)
print(tpl2)  # 输出：('h', 't', 't', 'p', 's', ':', '/', '/', 'm', 'p', '.', 'w', 'e', 'i', 'x', 'i', 'n', '.', 'q', 'q', '.', 'c', 'o', 'm', '/', 's', '/', '0', 'y', 'q', 'G', 'B', 'P', 'b', 'O', 'I', '6', 'Q', 'x', 'H', 'q', 'K', '1', '7', 'W', 'x', 'U', '8', 'Q')

# 如果参数已经是元组，则返回该元组的副本
tpl3 = (1, 2, 3, 4, 5)
tpl4 = tuple(tpl3)
print(tpl3 == tpl4)  # 输出：True
print(tpl3 is tpl4)  # 输出：True