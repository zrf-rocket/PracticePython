from inner_module_def_datastruct import WEIXIN_URL
# 1. 枚举列表中的元素
lst = ['a', 'b', 'c', 'd']
for i, x in enumerate(lst):
    print(i, x)  # 输出索引和元素

# 2. 枚举字符串中的字符
for i, c in enumerate(WEIXIN_URL):
    print(i, c)  # 输出索引和字符

# 3. 指定枚举的起始值
lst = ['python', 3.11, None, 'steverocket']
for i, x in enumerate(lst, start=1):
    print(i, x)  # 输出索引和元素，起始值为1
