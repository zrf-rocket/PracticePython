# @author:SteveRocket 
# @Date:2023/11/19
# @File:while-else
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

try:
    pass
except Exception as e:
    print(e)
else:
    print("this is else...")


count = 0
while count < 5:
    print(f"{count} is  less than 5")
    count = count + 1
else:
    print(f"{count} is not less than 5")


