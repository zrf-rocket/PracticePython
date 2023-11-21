# @author:SteveRocket 
# @Date:2023/11/19
# @File:while
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
i = 0
while i <= 10:
    print(i)
    i += 1

import requests

while True:
    response = requests.get("https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q")
    if response.status_code == 200:
        print(response.text)
        print("请求成功")
        break
    else:
        print("请求失败，重试")



# while 1:
#     print("死循环")
#
# while True:
#     print("死循环")

while 1:
    if i==10:
        pass
        # return  # SyntaxError: 'return' outside function
    i+=1

