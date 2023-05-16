# @author:SteveRocket 
# @Date:2023/5/14
# @File:def_reversed
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/

# 反转字典
user_dicts = {
    "author": "SteveRocket",
    "Date": "2023/5/14",
    "File": "def_reversed",
    "Email": "rocket_2014@126.com",
    "CSDN": "https://blog.csdn.net/zhouruifu2015/"
}
reversed_dicts = reversed(user_dicts)
print(reversed_dicts)
print(list(user_dicts.keys()))  # ['author', 'Date', 'File', 'Email', 'CSDN']
print(list(reversed_dicts))  # ['CSDN', 'Email', 'File', 'Date', 'author']


# 反转列表
user_infos = [
    "SteveRocket",
    "2023/5/14",
    "def_reversed",
    "rocket_2014@126.com",
    "https://blog.csdn.net/zhouruifu2015/"
]
reversed_infos = reversed(user_infos)
print(reversed_infos) # <list_reverseiterator object at 0x000001C3811A8F70>
print(list(reversed_infos)) # ['https://blog.csdn.net/zhouruifu2015/', 'rocket_2014@126.com', 'def_reversed', '2023/5/14', 'SteveRocket']


# 反转字符串
url = 'https://blog.csdn.net/zhouruifu2015/'
reversed_url = reversed(url)
print(reversed_url)  # <reversed object at 0x0000019A7B1C9640>
print(url)
for i in reversed_url:
    print(i, end='')
# /5102ufiuruohz/ten.ndsc.golb//:sptth
