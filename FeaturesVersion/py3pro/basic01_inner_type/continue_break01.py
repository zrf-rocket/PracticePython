# @author:SteveRocket 
# @Date:2023/10/17
# @File:continue_break01
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from FeaturesVersion import AGE, AUTHOR, BLOG

# SyntaxError: 'continue' not properly in loop
# if AGE > 18:
#     continue
# else:
#     break

for i in range(10):
    if i % 2:
        print("no something....")
        continue
    elif i > 9:
        break
    else:
        print(BLOG)
    print(i)