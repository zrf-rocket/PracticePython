# @author:SteveRocket 
# @Date:2023/11/19
# @File:for-else
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

for i in range(3):
    print(i, end=" ")
else:
    print("for循环语句执行完毕...")

from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Run Over Nothing....")

