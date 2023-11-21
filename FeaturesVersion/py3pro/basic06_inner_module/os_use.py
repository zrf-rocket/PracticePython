import os

pwd = os.getcwd()
print('当前路径', pwd)

os.chdir('..')
os.chdir('D:\steverocket')
# 在切换路径时，需要确保目标路径存在，否则会抛出异常
# os.chdir('D:\\is not exists')  # FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'D:\\tis not exists'
pwd2 = os.getcwd()
print('切换后的路径', pwd2)

os.chdir(pwd)
pwd3 = os.getcwd()
print('恢复后的路径', pwd3)