from inner_module_def_datastruct import AUTHOR, AGE, WEIXIN_URL, GENDER
import base64
import json

print(WEIXIN_URL)  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

# 字符串的Base64编码
encoded = base64.b64encode(WEIXIN_URL.encode('utf-8'))
print(encoded)  # b'aHR0cHM6Ly9tcC53ZWl4aW4ucXEuY29tL3MvMHlxR0JQYk9JNlF4SHFLMTdXeFU4UQ=='

# Base64编码的字符串解码
decoded = base64.b64decode(encoded).decode('utf-8')
print(decoded)  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q



# 读取文件内容并进行Base64编码
with open('./guide_imgs/wechat.png', 'rb') as wechat:
    content = wechat.read()
    encoded = base64.b64encode(content)
    print(encoded)  # b'iVBORw0KGgoAAAANSUhEUgA*****'

# Base64编码的字符串解码并保存为文件
decoded = base64.b64decode(encoded)
with open('./guide_imgs/wechat_back.png','wb') as wechat:
    wechat.write(decoded)



about_articulate_url = "https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q"

# URL安全的Base64编码
encoded = base64.urlsafe_b64encode(about_articulate_url.encode('utf-8'))
print(encoded)  # b'aHR0cHM6Ly9tcC53ZWl4aW4ucXEuY29tL3MvMHlxR0JQYk9JNlF4SHFLMTdXeFU4UQ=='

# URL安全的Base64编码的字符串解码
decoded = base64.urlsafe_b64decode(encoded).decode('utf-8')
print(decoded)  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q




def str2base64(data:str)->str:
    """
    编码
    """
    return str(base64.b64encode(data.encode('utf-8')), 'utf-8')

def base642str(base64_str:str)->str:
    """
    解码
    """
    return str(base64.b64decode(base64_str), 'utf8')

str_info = '{"name":"Cramer", "age": 25, "blog": None}'
dict_info = {"name":AUTHOR, "age": AGE, 'blog': WEIXIN_URL, 'gender':GENDER}

# 对字典字符串编码
str_info_base64_str = str2base64(str_info)
print(str_info_base64_str)  # eyJuYW1lIjoiQ3JhbWVyIiwgImFnZSI6IDI1LCAiYmxvZyI6IE5vbmV9

# 对字符串编码
str_info_str = base642str(str_info_base64_str)
print(type(str_info_str), str_info_str)  # <class 'str'> {"name":"Cramer", "age": 25, "blog": None}


# 先将字典转为字符串，使用separators=(',',':')去除空格
dict_info_str = json.dumps(dict_info, separators=(',', ':'))
print(type(dict_info_str), dict_info_str)
# 输出  <class 'str'> {"name":"SteveRocket","age":25,"blog":"https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q","gender":"M"}

dict_info_str_base64 = str2base64(dict_info_str)
print(type(dict_info_str_base64), dict_info_str_base64)
# 输出  <class 'str'> eyJuYW1lIjoiU3RldmVSb2NrZXQiLCJhZ2UiOjI1LCJibG9nIjoiaHR0cHM6Ly9tcC53ZWl4aW4ucXEuY29tL3MvMHlxR0JQYk9JNlF4SHFLMTdXeFU4USIsImdlbmRlciI6Ik0ifQ==

dict_info_dict = json.loads(base642str(dict_info_str_base64))
print(type(dict_info_dict), dict_info_dict)
# 输出  <class 'dict'> {'name': 'SteveRocket', 'age': 25, 'blog': 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q', 'gender': 'M'}



bytes_cnt = b"Hello SteveRocket"
print(type(bytes_cnt), bytes_cnt)  # <class 'bytes'> b'Hello SteveRocket'

# 编码二进制数据
encoded_data = base64.b64encode(bytes_cnt)
print(type(encoded_data), encoded_data) # <class 'bytes'> b'SGVsbG8gU3RldmVSb2NrZXQ='

# 解码二进制数据
decoded_data = base64.b64decode(encoded_data)
print(type(decoded_data), decoded_data)  # <class 'bytes'> b'Hello SteveRocket'


url = bytes("https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q", encoding='utf-8')
print(type(url), url)

# 二进制URL安全的编码
url_encoded = base64.urlsafe_b64encode(url)
print(type(url_encoded),url_encoded)
# 输出：<class 'bytes'> b'aHR0cHM6Ly9tcC53ZWl4aW4ucXEuY29tL3MvMHlxR0JQYk9JNlF4SHFLMTdXeFU4UQ=='

# 二进制URL安全的解码
url_decoded = base64.urlsafe_b64decode(url_encoded)
print(type(url_decoded), url_decoded)
# 输出：<class 'bytes'> b'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q'