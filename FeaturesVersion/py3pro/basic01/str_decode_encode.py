# @author:SteveRocket 
# @Date:2023/11/21
# @File:str_decode_encode
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
str = "微信公众号：CTO Plus"
encoded_str = str.encode('utf-8')
print(encoded_str)  # b'\xe5\xbe\xae\xe4\xbf\xa1\xe5\x85\xac\xe4\xbc\x97\xe5\x8f\xb7\xef\xbc\x9aCTO Plus'
decoded_str = encoded_str.decode('utf-8')
print(decoded_str)  # 微信公众号：CTO Plus
