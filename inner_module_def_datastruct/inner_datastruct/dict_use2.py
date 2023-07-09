# @author:SteveRocket 
# @Date:2023/7/6
# @File:dict_use2
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/

l1 = [11, 22, 33]
l2 = [1.1, 2.2, False]
l3 = ('name', 'score', 'is_node')
l4 = ['中文', 'Chinese']
print(list(zip(l1, l2, l3)))  # [(11, 1.1, 'name'), (22, 2.2, 'score'), (33, False, 'is_node')]

print(list(zip(l1, l2, l4)))  # [(11, 1.1, '中文'), (22, 2.2, 'Chinese')]

print(dict(zip(l1, l2)))  # {11: 1.1, 22: 2.2, 33: False}
# print(dict(zip(l1, l2, l4))) # ValueError: dictionary update sequence element #0 has length 3; 2 is required



person = {"name": "SteveRocket", "desc": "Python3.11 dict", "url": "https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q"}
informations = "abc"
print(dict(zip(person, informations)))

names = ['steverocket', 'cramer', 'zhangsan']
ages = {22, 23, 24}
salary = (3333, 4444, 5555)
print(dict(zip(names, salary))) # {'steverocket': 3333, 'cramer': 4444, 'zhangsan': 5555}

for name, age in zip(names, ages):
    print(f"{name} age is: {age}")
# steverocket age is: 24
# cramer age is: 22
# zhangsan age is: 23



# zip实现键值对反转
person = {"name": "SteveRocket", "desc": "Python3.11 dict", "url": "https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q", "alias": "SteveRocket"}
print(dict(zip(person.values(),person.keys())))
# {'SteveRocket': 'alias', 'Python3.11 dict': 'desc', 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q': 'url'}



salarys = {1 : 2222, 5 : 87665, 3 : 3454, 0 : 34345}
print(salarys)  # {1: 2222, 5: 87665, 3: 3454, 0: 34345}
print(sorted(salarys)) # [0, 1, 3, 5]
print(sorted(salarys, reverse=False))  # [0, 1, 3, 5]
print(sorted(salarys, reverse=True))  # [5, 3, 1, 0]
# 对key进行排序
for key in sorted(salarys):
    print(f"{key} : {salarys[key]}")
# 0 : 34345
# 1 : 2222
# 3 : 3454
# 5 : 87665


# 对value进行排序
salarys = {1 : 2222, 5 : 87665, 3 : 3454, 0 : 3454}
reverse_salarys = dict(zip(salarys.values(),salarys.keys()))
for salarys_value in sorted(reverse_salarys):
    print(f"{salarys_value} : {reverse_salarys[salarys_value]}")
# 2222 : 1
# 3454 : 0
# 87665 : 5


for key in sorted(salarys, key=lambda k:salarys[k]):
    print(f"{salarys[key]} : {key}")
# 2222 : 1
# 3454 : 3
# 3454 : 0
# 87665 : 5



d1 = {'key1':1, 'key2':7}
d2 = {'key1':3, 'key3':4}
# print(d1.values() & d2.values())  # TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values'
print(d1.keys() & d2.keys())  # {'key1'}
print(d1.keys() - d2.keys())  # {'key2'}
print(d1.keys() | d2.keys())  # {'key1', 'key2', 'key3'}


# 字典推导式
ages = {'steverocket':22, 'cramer':23, 'zhangsan':24}
print({k:v for k,v in ages.items() if v<=23})  # {'steverocket': 22, 'cramer': 23}



from operator import itemgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
print(sorted(rows, key=itemgetter('fname')))
print(sorted(rows, key=itemgetter('uid')))

print(sorted(rows, key=itemgetter('lname', 'fname')))

d1 = [{'key1':2}, {'key1':3}, {'key2': 2}, {'key3':4}]
print(list(set(val for dict in d1 for val in dict.values())))  # [2, 3, 4]
print(list(set(val for dict in d1 for val in dict.keys())))  # ['key2', 'key1', 'key3']
