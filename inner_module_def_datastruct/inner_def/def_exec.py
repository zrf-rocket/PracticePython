from inner_module_def_datastruct import WEIXIN_URL
result = eval('2 + 3 * 4')
print(result)  # 输出结果是14

exec('print(2 + 3 * 4)')  # 14

# 1. 动态生成函数
code = '''
def add(x, y):
    return x + y
'''

exec(code)
print(add(22, 33))  # 输出结果是5

# 2. 动态修改全局变量
x = 1
code = '''
x = WEIXIN_URL
'''

exec(code)
print(x)  # 输出结果是 https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

# 3. 动态执行复杂的Python代码
code = '''
for i in range(10):
    print(i, end=' ')
'''

exec(code)  # 0 1 2 3 4 5 6 7 8 9
