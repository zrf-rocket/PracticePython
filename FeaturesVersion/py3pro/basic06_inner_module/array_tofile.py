# @author:SteveRocket 
# @Date:2023/5/12
# @File:array_1
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/

import array

arr = array.array('i', [11, 22, 33, 44, 55, 66])
with open('data.bin', 'wb') as f:
    arr.tofile(f)

arr2 = array.array('i')
with open('data.bin', 'rb') as f:
    arr2.fromfile(f, 5)
print(arr2)
