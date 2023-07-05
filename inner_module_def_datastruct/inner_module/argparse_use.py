from inner_module_def_datastruct import AUTHOR

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




# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))




# parser = argparse.ArgumentParser(description='Demo1.')
# parser.add_argument('-f', '--file', help='input file path')
#
# # add_subparsers方法用于定义解析嵌套子命令的功能。它允许程序支持多个子命令，每个子命令都有自己的参数集合。
# subparsers = parser.add_subparsers(title='subcommands')
#
# # add_mutually_exclusive_group方法用于定义互斥的命令行参数集合。这意味着同一时间只能指定其中一个参数，否则会抛出错误。
# group = parser.add_mutually_exclusive_group()
# group.add_argument('-a', '--option_a', help='option A')
# group.add_argument('-b', '--option_b', help='option B')
# # group.add_argument('-b', '--option_b', help='option B2')  # 抛出异常  argparse.ArgumentError: argument -b/--option_b: conflicting option strings: -b, --option_b
#
# # argparse.ArgumentParser类的add_argument_group()方法用于创建和管理参数的分组。可以在命令行解析器中使用多个参数组，以便对相关参数进行组织和管理。
# group = parser.add_argument_group('Group Name')
# group.add_argument('-aa', '--option_aa', help='option A2')
#
# # parse_known_args()方法与parse_args()类似，但是它可以接受未知的命令行参数。它会将未知参数解析并返回，而不抛出错误。
# know_args, unknown = parser.parse_known_args()
# print(know_args, unknown)  # Namespace(file=None, option_a=None, option_aa=None, option_b=None) []
#
#
# # parse_intermixed_args()方法允许解析器在混合参数（终端位置参数和可选参数）的情况下执行解析。可以在无需显式声明参数类型的情况下解析参数。
# # intermixed_args = parser.parse_intermixed_args()
# # print(intermixed_args.option_a)
#
# # parse_known_intermixed_args()方法与parse_intermixed_args()类似，但它可以接受未知的命令行参数，并将其一起返回。
# # known_intermixed_args, unknown = parser.parse_known_intermixed_args()
# # print(known_intermixed_args, unknown)
#
# # parse_args是ArgumentParser的方法，用于解析命令行参数并返回一个包含所有参数值的命名空间对象。
# args = parser.parse_args()
#
# print(args)