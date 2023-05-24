# @author:SteveRocket 
# @Date:2023/5/20
# @File:str_type
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/

num_str ='123'
# 字符串长度不足 前面补0
print(num_str.zfill(5))   # 00123

num_str ='abc'
print(num_str.zfill(5)) # 00abc

num_str ='12345678'
print(num_str.zfill(5))  # 12345678

