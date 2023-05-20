# @author:SteveRocket 
# @Date:2023/5/20
# @File:def_memoryview
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/

# memoryview()函数的使用示例
my_list = [1, 2, 3, 4, 5]

# 创建一个内存视图对象
my_view = memoryview(bytearray(my_list))

# 对内存视图对象进行切片操作
my_slice = my_view[1:3]
print(my_slice, type(my_slice)) #<memory at 0x000002742382F280> <class 'memoryview'>

# 对内存视图对象进行赋值操作
my_view[2] = 10

print(my_list)  # 输出：[1, 2, 3, 4, 5]

print(list(my_view), type(my_view))  # [1, 2, 10, 4, 5] <class 'memoryview'>
