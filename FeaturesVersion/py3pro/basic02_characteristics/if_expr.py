# @author:SteveRocket 
# @Date:2023/6/24
# @File:if_expr
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
from FeaturesVersion import AGE

# 数值类型的判断
if AGE:
    print("age =", AGE)  # age = 28
# bool类型的判断
if True:
    print("is true")
# 字符串的判断
if "SteveRocket":
    print("nyname is steverocket")
# 列表的判断
if [1,2,3,4]:
    print("is list")
# 集合的判断
if {1,2,3}:
    print('is set')
# 字典的判断
if {1:1,2:2}:
    print('is dict')
# 对象的判断
if object:
    print('is object')
# 比较运算符判断
if AGE == 28:
    print('等于28')
if AGE > 18:
    print('大于18')
# 使用逻辑非判断
if not AGE < 18:
    print('大于18')


x = 10
y = 5
if x > 0 and y > 0:
    print("Both x and y are positive")



age = 25
if age >= 18:
    print("您已经成年了！")  # 您已经成年了！
else:
    print("您还未成年！")

# 上述代码中，根据变量`age`的值，通过条件判断来确定输出的结果。如果`age`大于等于18，则输出"您已经成年了！"，否则输出"您还未成年！"。


number1 = 55
number2 = 100

if number1 % 2:
    print('number is odd')   # number is odd
else:
    print('number is even')

if number2 % 2:
    print('number is odd')
else:
    print('number is even')  # number is even


x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


number = int(input('请输入任意一个正整数：'))
# 通过raw_input()输入的数字是字符串，然后使用int()将该字符串转化为整数
# py2中也可以使用raw_input() 但py3中无法使用
if number > AGE:
    print('比我年龄大:', number-AGE)
elif number == AGE:
    print('你跟我同龄')
else:
    print('你小我：', AGE-number, '岁')