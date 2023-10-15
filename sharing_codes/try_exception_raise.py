# @author:SteveRocket 
# @Date:2023/6/17
# @File:try_exception_raise
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/

try:
    # 可能会引发异常的代码块
    num = int(input("请输入一个数字: "))
    result = 10 / num
    print("计算结果:", result)

except ValueError:
    # 处理值错误异常
    print("输入的不是有效的数字")

except ZeroDivisionError:
    # 处理除零错误异常
    print("除数不能为零")

except Exception as e:
    # 处理其他异常
    print("发生了异常:", str(e))

finally:
    # 无论是否发生异常，都会执行的代码块
    print("异常处理完毕")



print(10 * (1/0))  # ZeroDivisionError: division by zero

print(4 + spam * 3)  # NameError: name 'spam' is not defined

print('2' + 2)  # TypeError: can only concatenate str (not "int") to str



try:
    number = int(input("请输入数字: "))
    print("数字:", number)
    print(100/number)
except (ValueError, ZeroDivisionError):
    print("不是数值类型 或 不可以为零的错误")
except:
    print("可选的未知错误！")
    raise '不可预知的错误类型'  # 重新抛出这个异常



raise NameError('SteveRocket')



try:
    raise KeyError('name not exists')
except KeyError as e:
    print('key错误', e)
    raise



number = int(input("请输入一个数值类型的内容："))
print("您输入的内容为：", number)
print("程序执行完毕....")


try:
    number = int(input("请输入一个数值类型的内容："))
    print("您输入的内容为：", number)
    print("程序执行完毕....")
except ValueError:
    print("您输入的内容有误，程序将退出")
print("程序执行完毕....")



try:
    number = int(input("请输入一个数值类型的内容："))
    print("您输入的内容为：", number)
    print("程序执行完毕....")
except ValueError as e:
    print("您输入的内容有误，程序将退出，错误信息：", e)
print("程序执行完毕....")



import sys

try:
    with open('steverocket.txt') as f:
        int(f.readline().strip())
except (IOError, OSError) as err:
    print("读取文件错误: {0}".format(err))
except ValueError:
    print("内容值错误")
# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
except (RuntimeError, TypeError, NameError):
    pass
except Exception as e:
    print("捕获所有异常", e)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
