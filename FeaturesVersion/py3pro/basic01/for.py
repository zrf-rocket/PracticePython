# @author:SteveRocket 
# @Date:2023/11/19
# @File:for
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

for i in "Steverocket":
    print(i, end=" ")
print()

for i in "微信公众号：CTO Plus":
    print(i, end=" ")
print()

for i in [28, "SteveRocket", {11,22}]:
    print(i, end=" ")

print(range(1, 5))


for i in range(1, 11):
    print(i)


sum = 0
for x in range(101):
    sum += x
print(sum)



for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()

