# @author:SteveRocket 
# @Date:2023/5/14
# @File:def__import__
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/

# __import__()函数的使用示例
# 导入模块
math = __import__("math")
print(math.sin(1.0))  # 输出：0.8414709848078965

os = __import__('os')
print(os.path.exists("def__import__.py"))

# 指定导入的模块名、导入的路径、导入的包等信息
importer = __import__("os.path", fromlist=[""])
print(importer.abspath("."))  # 输出：代码执行的当前路径
