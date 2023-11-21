# @author:SteveRocket 
# @Date:2023/11/22
# @File:str-demo1
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
str1 = 'hello, SteveRocket! 欢迎关注公众号：CTO Plus'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 36
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, steverocket! 欢迎关注公众号：cto plus
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, Steverocket! 欢迎关注公众号：Cto Plus
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, STEVEROCKET! 欢迎关注公众号：CTO PLUS
# 从字符串中查找子串所在位置
print(str1.find('rocket')) # -1
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('rocket'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # False
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))  # *******hello, SteveRocket! 欢迎关注公众号：CTO Plus*******

str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  rocket_2014@126.com '
print(str3) #   rocket_2014@126.com
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())# rocket_2014@126.com


msg = "欢迎关注公众号：CTO Plus"
print(msg[-1])  # 输出s
print(msg[-2])  # 输出u

msg = "欢迎关注公众号：CTO Plus"
print(msg[1:3])  # 迎关
print(msg[0:3:2])  # 欢关

msg = "欢迎关注公众号：CTO Plus"
print(msg[::-1]) # sulP OTC：号众公注关迎欢










