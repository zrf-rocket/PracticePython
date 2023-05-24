from inner_module_def_datastruct import WEIXIN_URL
# 1. 计算数学表达式
result = eval('2 + 3 * 4')
print(result)  # 输出结果是14


# 2. 执行Python代码
code = '''
def add(x, y): 
    return x + y
print(add(2, 3))
'''
exec(code)  # 输出 5
# eval(code)  # SyntaxError: invalid syntax
eval(compile(code, '<string>', 'eval')) # SyntaxError: invalid syntax

eval('print(WEIXIN_URL)')  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q


# 3. 动态生成字典或列表
lst = eval('[1, 2, 3]')
print(lst, type(lst))  # 输出结果是[1, 2, 3]

dct = eval('{"a": 1, "b": 2, "c": 3}')
print(dct, type(dct))  # 输出结果是{"a": 1, "b": 2, "c": 3}
