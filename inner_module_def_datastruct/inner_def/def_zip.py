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




