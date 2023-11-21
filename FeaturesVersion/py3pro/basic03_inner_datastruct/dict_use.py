# @author:SteveRocket 
# @Date:2023/6/6
# @File:dict_use
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
from inner_module_def_datastruct import WEIXIN_URL
empty_dict = {}
print(type(empty_dict), empty_dict) # <class 'dict'> {}

empty_dict2 = dict()
empty_dict2['key5'] = 1
print(type(empty_dict2), empty_dict2) # <class 'dict'> {'key5': 1}

person = {'name': 'SteveRocket', 'age': 25, 'gender': True}

d1 = {'key3': ('this is tuple'), 'key2': {'info':'this is sub dict'}, 'key1': 4, 'numbers': [1, 2, 3, 4, 5]}
print(d1) # {'key3': 'this is tuple', 'key2': {'info': 'this is sub dict'}, 'key1': 4, 'numbers': [1, 2, 3, 4, 5]}



print(person['name']) # SteveRocket

print(person.get('name', 'unknown')) # SteveRocket
print(person.get('address', 'unknown')) # unknown



# 修改字典中value的元素
d1['numbers'][0] = 111
print(d1)  # {'key3': 'this is tuple', 'key2': {'info': 'this is sub dict'}, 'key1': 4, 'numbers': [111, 2, 3, 4, 5]}

print(person)  # {'name': 'SteveRocket', 'age': 25, 'gender': True}
person['age'] = 28
person['address'] = WEIXIN_URL
print(person)  # {'name': 'SteveRocket', 'age': 28, 'gender': True, 'address': 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q'}



del person['gender']
age = person.pop('age')
print(age)  # 28
print(person)  # {'name': 'SteveRocket', 'address': 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q'}




d = {"name": "SteveRocket", "desc": "Python3.11 dict", "url":"https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q"}
print("d：", d)  # d： {'name': 'Steverocket', 'desc': 'Python3.11 dict', 'url': 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q'}
# 如果字典不存在update中的键值对，则向字典中插入新的键值对
ages = {"ages": 25}
d.update(ages)
print("d：", d)  # d： {'name': 'Steverocket', 'desc': 'Python3.11 dict', 'url': 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q', 'ages': 25}

ages2 = {"ages": 28}
d.update(ages2)
print("d：", d) # d： {'name': 'Steverocket', 'desc': 'Python3.11 dict', 'url': 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q', 'ages': 28}

print(list(person.values()))  # ['SteveRocket', 25, True]
# print(person['blog'])  # KeyError: 'blog'
print('name' in person)  # True
print('blog' in person) # False


for key, value in person.items():
    print(key, value)

for i, key in enumerate(person):
    print(i, key, person.get(key, None))

for key in person:
    print(key, person.get(key))
# 输出所有的键值对，并遍历
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

print(person)


print(person.update({'blog':WEIXIN_URL}))  # None
print(person)  # {'name': 'SteveRocket', 'age': 25, 'gender': True, 'blog': 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q'}
person.clear()
print(person)  # {}
