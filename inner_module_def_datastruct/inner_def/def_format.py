from inner_module_def_datastruct import WEIXIN_URL
# 1. 格式化数字
n = 3.1415926
# 保留输出的小数点位数
s = 'pi is {:.2f}'.format(n)
print(s)  # 输出结果是'pi is 3.14'


# 2. 格式化字符串
name = 'SteveRocket'
age = 25
s = '{} is {} years old'.format(name, age)
print(s)  # 输出结果是'SteveRocket is 25 years old'
s2 = '{name} {age}'.format(age=age, name=name)
print(s2)  # SteveRocket 25
s3 = '{1} {0}'.format(name, age)
print(s3) # 25 SteveRocket


# 3. 格式化列表
lst = [1, 2, 3, 4]
s = 'the list is {}'.format(lst)
print(s)  # 输出结果是'the list is [1, 2, 3, 4]'


num_str = 1234567.8901234  # 不能是字符串类型的数值
print('{:5.2f}'.format(num_str))    # 1234567.89
# 千位分隔符号输出
print('{:,}'.format(num_str))       # 1,234,567.8901234

# 百分号输出
print('{:.2%}'.format(num_str))  # 123456789.01%
print('{:.1%}'.format(num_str)) # 123456789.0%


print(f'this is my blog1 {WEIXIN_URL}')  # this is my blog1 https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q


format_str = 'this is my blog2 {}'.format
print(format_str(WEIXIN_URL)) # this is my blog2 https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q



num_str = 123.8234
# 给定一个数字 123456，请采用宽度为 25、右对齐方式打印输出，使用加号“+”填充。
print('{:+>25}'.format(num_str)) # +++++++++++++++++123.8234

# 给定一个数字 123456，请采用宽度为 25、右对齐方式打印输出，使用加号 空格 填充。
print('{: >25}'.format(num_str)) #                 123.8234

print('{:.25}'.format(num_str))  # 123.8234000000000065710992


# 给定一个数字，增加千位分隔符号，设置宽度为30、右对齐方式打印输出，使用空格填充。 ‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬
print('{:>30,}'.format(13245678.9))  # 输出：                  13,245,678.9

# 给定一个整数数字0x1010，请依次输出Python语言中十六进制、十进制、八进制和二进制表示形式，使用英文逗号分隔。
print('0x{0:x}, {0:}, 0o{0:o}, 0b{0:b}'.format(0x1010))  # 0x1010, 4112, 0o10020, 0b1000000010000

# 编写 Python 程序输出一个具有如下风格效果的文本，用作文本进度条样式，部分代码如下，填写空格处。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬
# 　　 10%@==
# 　　 20%@====
# 　　100%@====================
#
# 　　前三个数字，右对齐；后面字符，左对齐‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

# 文本中左侧一段输出N 的值，右侧一段根据N 的值输出等号，中间用 @ 分隔，等号个数为N 与 5 的整除商的值，例如，当N 等于 10 时，输出 2 个等号。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬
# N取值范围是0—100，整数
N = 10
print("{:>3}%@{}".format(N, "="*(N//5)))
N = 20
print("{:>3}%@{}".format(N, "="*(N//5)))
N = 100
print("{:>3}%@{}".format(N, "="*(N//5)))


# 根据输入字符串s，输出一个宽度为 15 字符，字符串 s 居中显示，以“=”填充的格式。如果输入字符串超过 15 个字符，则输出字符串前 15 个字符。提示代码如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬
s = '123.466'
print("{:=^15}".format(s[0:15]))  # ====123.466====
s = '1.1'
print("{:=^15}".format(s[0:15]))  # ======1.1======
s = '1234567890123450000'
print("{:=^15}".format(s[0:15]))  # 123456789012345