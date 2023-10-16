# @author:SteveRocket 
# @Date:2023/6/24
# @File:expr
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/

name = "SteveRocket"

alias, age, blog = name, 25, "https://blog.csdn.net/zhouruifu2015/"
print(id(alias) == id(name))  # True
print(alias, age, blog)  # SteveRocket 25 https://blog.csdn.net/zhouruifu2015/

infos = name, 25, "https://blog.csdn.net/zhouruifu2015/"
print(infos)  # ('SteveRocket', 25, 'https://blog.csdn.net/zhouruifu2015/')





