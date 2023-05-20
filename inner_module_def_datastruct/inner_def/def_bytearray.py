from inner_module_def_datastruct import WEIXIN_URL
# 1. 创建一个空的字节数组对象
bt = bytearray()
print(bt, type(bt)) # bytearray(b'') <class 'bytearray'>

# 2. 通过一个字符串初始化字节数组
bt = bytearray(WEIXIN_URL, 'utf-8')
print(bt) # bytearray(b'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q')

# 3. 通过一个字节序列初始化字节数组
bt = bytearray(b'\x01\x02\x03')
print(bt) # bytearray(b'\x01\x02\x03')

# 4. 通过一个可迭代对象初始化字节数组
bt = bytearray([1, 2, 3])
print(bt) # bytearray(b'\x01\x02\x03')

# 5. 通过一个整数指定字节数组的长度
bt = bytearray(5)
print(bt) # bytearray(b'\x00\x00\x00\x00\x00')

# 6. 修改字节数组中的值
bt[0] = 10
print(bt) # bytearray(b'\n\x00\x00\x00\x00')