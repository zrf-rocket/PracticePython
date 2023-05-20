from inner_module_def_datastruct import WEIXIN_URL
# 1. 编译Python代码字符串为可执行代码对象
code_obj = compile('print(f"Hello, this is my blog {WEIXIN_URL}")', '<string>', 'exec')
# 执行代码对象
exec(code_obj)  # Hello, this is my blog https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q


# 2. 编译Python文件为可执行代码对象
with open('compile_test.py', 'r') as f:
    code_str = f.read()

code_obj = compile(code_str, 'compile_test.py', 'exec')
# 执行代码对象
exec(code_obj)  # this is my blog https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q


# 3. 编译Python表达式为可执行代码对象
code_obj = compile('1 + 2', '<string>', 'eval')
result = eval(code_obj)  # 执行代码对象
print(result)  # 输出结果是3
