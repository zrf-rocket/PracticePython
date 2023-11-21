# https://blog.csdn.net/zhouruifu2015/article/details/50855610
import hashlib

# 文件路径
file_path = "D:\steverocket\CentOS7_back.zip"

def file_md5(file_name):
    """
    参数：文件名
    return: 获取zip文件的md5
    """
    with open(file_name, "rb") as f:
        content = f.read()
        m = hashlib.md5()
        m.update(content)
        return m.hexdigest()

print(file_md5(file_path))



def calc_md5():
    # 打开文件
    with open(file_path, 'rb') as f:
        # 创建MD5对象
        md5_obj = hashlib.md5()

        # 读取文件内容，更新MD5对象
        while 1:
            data = f.read(4096)  # 每次读取4096字节
            if not data:
                break
            md5_obj.update(data)

    # 获取MD5值
    md5_value = md5_obj.hexdigest()
    print(md5_value)
