# @author:SteveRocket 
# @Date:2023/5/14
# @File:def_zip
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/


# zip()函数的使用示例
# 合并两个列表
lst1 = [1, 2, 3]
lst2 = ["SteveRocket", "rocket_2014@126.com", "https://blog.csdn.net/zhouruifu2015/"]
result = zip(lst1, lst2)
print(list(result))  # 输出：[(1, 'SteveRocket'), (2, 'rocket_2014@126.com'), (3, 'https://blog.csdn.net/zhouruifu2015/')]

# 合并三个列表
lst1 = [3.11, 2, 3]
lst2 = ["python", "b", "c"]
lst3 = ["SteveRocket", "zip", "def"]
result = zip(lst1, lst2, lst3)
print(list(result))  # 输出：[(3.11, 'python', 'SteveRocket'), (2, 'b', 'zip'), (3, 'c', 'def')]

# 如果可迭代对象的长度不一致，则以最短的可迭代对象为准
lst1 = ['protocol', 'domain', 'author', 'date']
lst2 = ["https", "blog.csdn.net", "zhouruifu2015"]
result = zip(lst1, lst2)
print(list(result))  # 输出：[('protocol', 'https'), ('domain', 'blog.csdn.net'), ('author', 'zhouruifu2015')]


str1 = "SteveRocket"
str2 = "Cramer"
# 直接输出或使用str进行转换  返回的都是zip对象
print(zip(str1, str2))  # <zip object at 0x000001FCFDB5F2C0>
print(str(zip(str1, str2))) # <zip object at 0x000001FCFDB5F2C0>
# 可以使用list或遍历的方式 输出zip的内容
print(list(zip(str1, str2)))  # [('S', 'C'), ('t', 'r'), ('e', 'a'), ('v', 'm'), ('e', 'e'), ('R', 'r')]



dict1 = {"name1":"SteveRocket","age1":25}
dict2 = {"name2":"Cramer","age2":22}
print(list(zip(dict1.values(), dict2.values())))  # [('SteveRocket', 'Cramer'), (25, 22)]
print(list(zip(dict1, dict2)))  # [('name1', 'name2'), ('age1', 'age2')]



tuple1 = ("SteveRocket", "Cramer")
tuple2 = (25, 22)
print(list(zip(tuple1, tuple2)))  # [('SteveRocket', 25), ('Cramer', 22)]



z1 = zip([1,2,3,4])
z2 = zip([11,21,31,41])
print(list(zip(z1, z2)))  # [((1,), (11,)), ((2,), (21,)), ((3,), (31,)), ((4,), (41,))]



person = {"name": "SteveRocket", "desc": "Python3.11 dict", "url": "https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q"}
informations = "abc"
print(list(zip(person, informations)))  # [('name', 'a'), ('desc', 'b'), ('url', 'c')]
print(dict(zip(person, informations))) # {'name': 'a', 'desc': 'b', 'url': 'c'}