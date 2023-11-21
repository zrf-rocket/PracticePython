# @author:SteveRocket 
# @Date:2023/6/24
# @File:while_expr
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/

fruits = ["apple", "banana", "cherry"]

while fruits:
    print(fruits.pop())

# 上述代码中，通过`while`循环遍历列表`fruits`中的元素，并将变量`fruits`中的每个元素从后面依次弹出，然后打印输出，直到列表中的元素为空，则停止while循环。