# @author:SteveRocket 
# @Date:2023/10/16
# @File:variable01
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

age = 28
name = "steverocket"
blog = "https://mp.weixin.qq.com/s/V5Axn-ZWi22ubh5Jiocb9g"

PI = 3.14159
MAX_SIZE = 100

number1 = 123456789
number2 = 987654321
print(number1 + number2)  # 1111111110
print(number1 - number2)  # -864197532
print(number1 * number2)  # 121932631112635269
print(number1 / number2)  # 0.1249999988609375

# 不同类型的数值进行运算（这点与Golang就非常不一样）
print(PI + age)  # 31.14159
print(PI * age)  # 87.96452

from FeaturesVersion import AGE, AUTHOR, BLOG

number = 1 + 5j
is_gender = True
print(type(AGE))  # <class 'int'>
print(type(PI))  # <class 'float'>
print(type(BLOG))  # <class 'str'>
print(type(number))  # <class 'complex'>
print(type(is_gender))  # <class 'bool'>

# 将变量的类型拿来比较
print(type(AUTHOR) == type(BLOG))  # True
print(type(AUTHOR) is type(BLOG))  # True

print(type(AGE) == type(BLOG))  # False
print(type(AGE) is type(BLOG))  # False

new_pi = int(PI)
# float转int
print(new_pi, type(new_pi))  # 3 <class 'int'>

number = "123456.6789"
print(number, type(number))  # 123456.6789 <class 'str'>
# str转float
new_number_f = float(number)
print(new_number_f, type(new_number_f))  # 123456.6789 <class 'float'>
# str转int
# number = "123456.6789" 或 "123456."  使用int转换会报错  ValueError: invalid literal for int() with base 10: '123456.6789'
number = "123456"
new_number_i = int(number)
print(new_number_i, type(new_number_i))  # 123456 <class 'int'>
# print(int("1234s"))  # ValueError: invalid literal for int() with base 10: '1234s'


# 分别将int和float的数值转为str
new_number_s1 = str(new_number_i)
new_number_s2 = str(new_number_f)
print(new_number_s1, type(new_number_s1))  # 123456 <class 'str'>
print(new_number_s2, type(new_number_s2))  # 123456.6789 <class 'str'>


str = "微信公众号：CTO Plus"
str_to_list = list(str)
print(type(str_to_list), str_to_list)  # <class 'list'> ['微', '信', '公', '众', '号', '：', 'C', 'T', 'O', ' ', 'P', 'l', 'u', 's']


lis = [11, 22, 33]
lis_to_tuple = tuple(lis)
print(type(lis_to_tuple), lis_to_tuple) # <class 'tuple'> (11, 22, 33)


lst = [("name", "SteveRocket"), ("age", AGE)]
dic = dict(lst)
print(type(dic), dic) # <class 'dict'> {'name': 'SteveRocket', 'age': 28}


# chr()
num1, num2, num3 = 45, 46, 47
num1_c, num2_c, num3_c = chr(num1), chr(num2), chr(num3)
print(num1_c, num2_c, num3_c)  # - . /
print(type(num1_c), type(num2_c), type(num3_c))  # <class 'str'> <class 'str'> <class 'str'>

# ord()
chr1, chr2, chr3, chr4 = 'a', 'A', 'B', 'C'
print(ord(chr1), ord(chr2), ord(chr3), ord(chr4))  # 97 65 66 67
print(type(ord(chr1)))  # <class 'int'>


# 区分大小写的变量
num = 123
Num = 456
print(num)  # 123
print(Num)  # 456

e1 = eval("123")
e2 = eval("12.3")
# e3 = eval("12.3.455") # SyntaxError: invalid syntax
# e3 = eval(BLOG)  # SyntaxError: invalid character '：' (U+FF1A)
# e3 = eval("hello steverocket")   # SyntaxError: invalid syntax
e3 = eval(28)  # TypeError: eval() arg 1 must be a string, bytes or code object
print(e1, e2) # 123 12.3
print(type(e1), type(e2)) # <class 'int'> <class 'float'>



'''
这是一个多行注释
可以跨越多行
'''
def add(x, y):
    """
    这是一个函数的文档字符串
    用于对函数进行解释和说明
    """
    return x + y
