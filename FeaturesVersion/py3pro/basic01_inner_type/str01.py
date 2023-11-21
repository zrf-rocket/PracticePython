# @author:SteveRocket 
# @Date:2023/11/21
# @File:str01
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
s1 = """ """
s2 = ''
s3 = ""
s4 = ''''''
print(type(s1))  # <class 'str'>
print(type(s2))  # <class 'str'>
print(type(s3))  # <class 'str'>
print(type(s4))  # <class 'str'>

# 定义字符串变量
author = " SteveRocket "
email = "rocket_2014@126.com"
print(author)
print(email)
multi_line = """多行文档字符串
第二行
第三行"""
print(multi_line)


print(len(email))  # 19
platform = "微信公众号：CTO Plus"
print(platform[0])  # 微
print(platform[2])  # 公
print(len(platform))  # 14

print(platform[2:5])  # 公众号
print(platform[6:])  # CTO Plus

plat = "微信公众号："
name = "CTO Plus"
# 拼接字符串
new_platform = plat+name
print(len(new_platform), new_platform)  # 14 微信公众号：CTO Plus
print(name*5)  # CTO PlusCTO PlusCTO PlusCTO PlusCTO Plus



platform = "  微信公众号：CTO Plus   "
# 生成一个新的字符串 移除字符串左右两边的所有空格
print(f'\"{platform.strip()}\"') #"微信公众号：CTO Plus"
# 原始字符串不变
print(f"\'{platform}\'") #'  微信公众号：CTO Plus   '
# 移除字符串左边的所有空格
print(f"\'{platform.lstrip()}\'") # '微信公众号：CTO Plus   '
# 移除字符串右边的所有空格
print(f"\'{platform.rstrip()}\'")  # '  微信公众号：CTO Plus'
# 按照空格拆分字符串（从左边开始拆），生成一个列表
print(platform.split())  # ['微信公众号：CTO', 'Plus']
print(platform.split(" ", 1)) # ['', ' 微信公众号：CTO Plus   ']
# 按照空格拆分字符串（从右边开始拆），生成一个列表
print(platform.rsplit())  # ['微信公众号：CTO', 'Plus']
print(platform.rsplit(" ", 1)) # ['  微信公众号：CTO Plus  ', '']

# 字符串转小写
print(platform.lower()) #  微信公众号：cto plus
# 字符串转大写
print(platform.upper()) #  微信公众号：CTO PLUS
# 判断字符串是否是大写
print(platform.isupper()) # False
# 判断字符串是否是小写
print(platform.islower()) # False

from inner_module_def_datastruct import AUTHOR
author = AUTHOR
print(author) # SteveRocket
print(author.isupper()) # False
print(author.islower()) # False



blog = "https://blog.csdn.net/zhouruifu2015/"
# 查找字符串（从左边开始找）
print(blog.find("o"))  # 10
print(blog.find("steverocket")) # 未找到返回-1
# 查找字符串（从右边开始找）
print(blog.rfind("o"))  # 24

# 字符串替换
print(blog.replace("https","http")) # http://blog.csdn.net/zhouruifu2015/
# 如果要替换的字符串未找到 不会报错 而是原样输出
print(blog.replace("ftp", "http")) # https://blog.csdn.net/zhouruifu2015/

wechat = "https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q"

lis = ["steverocket", "28", "微信公众号：CTO Plus"] # 此处的数字28 必须是字符串的数字
print(" ".join(lis))  # steverocket 28 微信公众号：CTO Plus