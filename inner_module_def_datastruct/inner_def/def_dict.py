# dict() 函数用于创建一个字典。
# 用法
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)

# 参数说明：
# **kwargs -- 关键字。
# mapping -- 元素的容器，映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。
# iterable -- 可迭代对象。

print({})
print(dict())
print(dict({'name': 'rocket', 'email': 'rocket_2014@126.com', 'year': 2023}))
# 输出：{'name': 'rocket', 'email': 'rocket_2014@126.com', 'year': 2023}

# 1. 创建一个字典对象
print(dict(name="rocket", email="rocket_2014@126.com", year=2023))
# 输出：{'name': 'rocket', 'email': 'rocket_2014@126.com', 'year': 2023}

# 2. 映射函数方式来构造字典  zip() 创建可迭代对象
# 映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。
print(dict(zip(["name", "email", "year"], ("rocket", "rocket_2014@126.com", 2023))))
# 输出：{'name': 'rocket', 'email': 'rocket_2014@126.com', 'year': 2023}

# 可迭代对象方式来构造字典
print(dict([("name", "rocket"), ("email", "rocket_2014@126.com"), ("year", 2023)], language="python3.11"))
# 输出：{'name': 'rocket', 'email': 'rocket_2014@126.com', 'year': 2023, 'language': 'python3.11'}

# 3. 通过可迭代对象创建字典
l = [('a', 1), ('b', 2), ('c', 3)]
d = dict(l)
print(d)  # 输出结果是{'a': 1, 'b': 2, 'c': 3}