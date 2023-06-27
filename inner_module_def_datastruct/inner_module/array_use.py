# array模块是Python中的一个标准库，是一个预定义的数组，因此其在内存中占用的空间比标准列表小得多，同时也可以执行快速的元素级别操作，例如添加、删除、索引和切片等操作。
# array模块还支持将数组对象直接写入和读取到二进制文件中，这使得在处理大量数值数据时更加高效。因此，如果需要处理大量同质数据，可以考虑使用Python的array模块来优化代码的执行效率。

# 要使用array模块，首先需要导入它
import array

# 然后，可以使用array函数创建一个数组对象。array函数的第一个参数是数组的类型，指定数组中元素的类型，比如整数、浮点数、字符等等。取值为如下：
# b：signed char
# B：unsigned char
# h：signed short
# H：unsigned short
# i：signed integer
# I：unsigned integer
# l：signed long
# L：unsigned long
# q：signed long long
# Q：unsigned long long
# f：float
# d：double

# 第一个参数用于指定数组中的所有元素都是同一种类型，因此可以使用数组提供的高效数值运算函数，例如计算平均值、最大值和最小值等。
# a1 = array.array('i', [11, 22, 3.3, 44, 55])  # 由于第一个参数i决定了数组里面的元素类型，所以此处有3.3 即使是3.0  也会报错：TypeError: 'float' object cannot be interpreted as an integer
# Python创建数组：第1种方法
# 创建一个浮点型的数组
a = array.array('f', [11., 22., 3.0, 44., 55]) # 正常
# 创建一个包含5个整数的数组
a1 = array.array('i', [11, 22, 33, 44, 55]) # 正常

# Python创建数组：第2中方法
a2 = [11, 22, 33, 44, 55]
# Python创建数组：第3中方法
a3 = list([11, 22, 33, 44, 55])

print(type(a1), type(a2), type(a3))  # <class 'array.array'> <class 'list'> <class 'list'>
print(a1[1], a2[1], a3[1])  # 22 22 22

# 打印数组的元素
for x in a1:
    print(x)

# 在数组中添加元素，可以使用append方法：
a1.append(11) # 这将在数组的末尾添加一个元素。
print(a1)

# 还可以使用insert方法在指定位置插入一个元素：
a1.insert(55, 200)  # 如果指定插入的位置比数组本身长度都长，则直接在数组的末尾插入元素，而不会报错
a1.insert(5, 300) # 这将在数组的第6个位置插入一个值为100的元素。
a1.insert(0, 100) # 在数组的第一个位置插入元素
a1.insert(-1, 100) # 在数组的倒数第二个位置插入元素
print(a1)


# 要从数组中删除元素，可以使用remove方法：
a1.remove(100)
print(a1)  # 这将从数组中删除值为100的第一个元素。

# 还可以使用pop方法删除指定位置的元素：

print(a1.pop(5))  # 这将从数组中删除第6个元素，并返回该元素。
print(a1.pop())  # 如果不指定位置，pop方法将删除最后一个元素。
# print(a1.pop(111))  # 如果pop的位置大于数组长度，则会报错 IndexError: pop index out of range
print(a1)

# index



# count


# reverse