# @author:SteveRocket 
# @Date:2023/11/13
# @File:use_pkgs
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

# 引入模块say_hello，并将模块say_hello重命名为say_hello01
from utils01 import say_hello as say_hello01
# 引入模块say_hello，并将模块say_hello重命名为say_hello02
from utils02 import say_hello as say_hello02

print(say_hello01())
print(say_hello02())


from pkg01 import module01
# 使用 . 的方式调用模块中的方法
module01.function("Python3.12")
# 调用模块中的变量
print(module01.my_blog)

# 或者直接导入方法
from pkg01.module01 import function
function("Python3.13")

# 导入类
from pkg01.module01 import DemoClass
# 实例化对象
obj = DemoClass()
# 调用对象的方法
obj.show("my name is steverocket")
