from inner_module_def_datastruct import WEIXIN_URL, AUTHOR

# argparse 模块是 Python 内置的用于命令项选项与参数解析的模块，argparse 模块可以让人轻松编写用户友好的命令行接口，能够帮助程序员为模型定义参数。

# 导入argparse包
import argparse
# 创建一个命令行解析器对象 ArgumentParser()
parser = argparse.ArgumentParser(description='this is steverocket scripts')

# 给解析器添加命令行参数 add_argument() 用来添加参数
parser.add_argument('--num1', type=int, default=0)
parser.add_argument('--num2', type=int, default=2.2)
parser.add_argument('--author', type=str, default=AUTHOR)

# 从命令行中解析参数  parse_args()用来解析添加的（命令行）参数
args = parser.parse_args()
print(args, type(args))  # 默认输出：Namespace(num1=0, num2=2.2, author='SteveRocket') <class 'argparse.Namespace'>
print(args.num1, args.num2, args.author) # 默认输出： 0 2.2 SteveRocket
