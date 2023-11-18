# @author:SteveRocket 
# @Date:2023/11/18
# @File:demo6_
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
from inner_module_def_datastruct import WEIXIN_URL, AGE, CSDN_URL
# for _ in range(3):
#     print(WEIXIN_URL)


person = (AGE, CSDN_URL, WEIXIN_URL, "this is Python3.12")
age, _, _, msg = person
age2, _, weixin2, _ = person
print(age, msg)
print(age2, weixin2)