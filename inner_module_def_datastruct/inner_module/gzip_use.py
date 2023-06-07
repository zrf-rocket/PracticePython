# https://blog.csdn.net/zhouruifu2015/article/details/50909417

import gzip
SOURCE_FILE = "D:\steverocket\CentOS7.zip"
TARGET_FILE = "D:\steverocket\CentOS7.gz"

def compress_gzfile():
    with open(SOURCE_FILE, 'rb') as f_in:
        with gzip.open(TARGET_FILE, 'wb') as f_out:
            f_out.write(f_in.read())

TARGET_FILE_BACK = "D:\steverocket\CentOS7_back.zip"

def decompression_gzfile():
    with gzip.open(TARGET_FILE, 'rb') as f_in:
        with open(TARGET_FILE_BACK, 'wb') as f_out:
            f_out.write(f_in.read())

if __name__ == '__main__':
    # compress_gzfile()
    decompression_gzfile()