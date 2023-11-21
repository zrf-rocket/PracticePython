from inner_module_def_datastruct import WEIXIN_URL,CSDN_URL
# open()函数的使用示例
# 打开文件并写入内容
with open('test.txt', 'w') as f:
    f.write(WEIXIN_URL)

# 打开文件并读取内容
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)

# 打开文件并追加内容
with open('test.txt', 'a') as f:
    f.write(CSDN_URL)

# 打开二进制文件并读取内容
with open('test.bin', 'rb') as f:
    content = f.read()
    print(content)
