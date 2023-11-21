from inner_module_def_datastruct import WEIXIN_URL

# hash()函数的使用示例
print(hash("hello"))  # 8717829118467943447
print(hash((1, 2, 3)))  # 529344067295497451
print(hash(123))  # 123
print(hash(3.14))  # 476876632144354977
print(hash(True))  # 1
print(hash(False))  # 0

# 不可哈希的对象示例
# print(hash([1, 2, 3]))  # TypeError: unhashable type: 'list'
# print(hash({"name": "SteveRocket", "age": 18}))  # TypeError: unhashable type: 'dict'

# 哈希值相同的对象示例
print(hash("hello"))  # 8717829118467943447
print(hash("Hello"))  # 3152661429459725354

# 哈希值不同的对象示例
print(hash("hello"))  # 8717829118467943447
print(hash("world"))  # -7160543189288757831

# 对URL进行hash
print('URL', hash(WEIXIN_URL))  # URL 7620566311523340584
print('空字符串：', hash(''))   # 空字符串： 0
print('None', hash(None))   # None 8795438377352