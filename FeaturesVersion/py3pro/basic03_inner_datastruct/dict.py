# 比较运算
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
print(dict1 == dict2)

# 成员运算
print("a" in dict1)  # 输出：True
print("c" not in dict1)  # 输出：True


# 逻辑运算
dict3 = {"c": 3}
print(dict1 and dict3)  # 输出：{'c': 3}
print(dict1 or dict3)  # 输出：{'a': 1, 'b': 2}


# 按键排序
person = {"name": "Cramer", "age": "25", "gender": "female"}
sorted_keys = sorted(person.keys())
print(sorted_keys)  # 输出：['age', 'gender', 'name']

# 按值排序
sorted_values = sorted(person.values())
print(sorted_values)  # 输出：["25", 'Cramer', 'female']
# 注意：如果age中的25是数字  则会抛异常：TypeError: '<' not supported between instances of 'int' and 'str'


sorted_items = sorted(person.items(), key=lambda x: x[0])
print(sorted_items)  # [('age', '25'), ('gender', 'female'), ('name', 'Cramer')]
print(dict(sorted_items))  # {'age': '25', 'gender': 'female', 'name': 'Cramer'}

names = ["SteveRocket", "Cramer", "Zhangsan"]
ages = [25, 22, 35]
person_dict = list(map(lambda x: {"name": x[0], "age": x[1]}, zip(names, ages)))
print(person_dict)
# [{'name': 'SteveRocket', 'age': 25}, {'name': 'Cramer', 'age': 22}, {'name': 'Zhangsan', 'age': 35}]

