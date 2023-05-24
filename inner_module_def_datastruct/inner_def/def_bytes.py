from inner_module_def_datastruct import WEIXIN_URL
# 1. 创建一个空的字节序列对象
b = bytes()
print(b, type(b), len(b))  # b'' <class 'bytes'> 0

# 2. 通过一个字符串初始化字节序列
b = bytes(WEIXIN_URL, 'utf-8')
print(b, type(b), len(b))  # b'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q' <class 'bytes'> 49
for i in b:
    print(i, end=' ')

# 3. 通过一个字节序列初始化字节序列
b = bytes(b'\x01\x02\x03')
print(b, type(b), len(b)) # b'\x01\x02\x03' <class 'bytes'> 3

# 4. 通过一个可迭代对象初始化字节序列
b = bytes([1, 2, 3])
print(b, type(b), len(b)) # b'\x01\x02\x03' <class 'bytes'> 3

# 5. 通过一个整数指定字节序列的长度
b = bytes(5)
print(b, type(b), len(b))  # b'\x00\x00\x00\x00\x00' <class 'bytes'> 5

# 6. 访问字节序列中的值
print(b[0])  # 返回值是0

# 遍历字节序列
for i in b:
    print(i, end=' ') # 0 0 0 0 0
