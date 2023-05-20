print(globals())  # 输出系统的所有内置全部变量

# 1. 获取全局变量的值
x = 10
y = 20
globals_dict = globals()
x_val = globals_dict['x']
y_val = globals_dict['y']
print(x_val, y_val)  # 输出结果是10 20

# 2. 修改全局变量的值
x = 10
globals_dict = globals()
globals_dict['x'] = 20
print(x)  # 输出结果是20

# 3. 遍历全局变量
globals_dict = globals()
print(type(globals_dict))

# RuntimeError: dictionary changed size during iteration
# for key, value in globals_dict.items():
#     try:
#         print(key, str(value))
#     except RuntimeError as e:
#         print(e)

# RuntimeError: dictionary changed size during iteration
# for index, key in enumerate(globals_dict):
#     try:
#         print(index, key, globals_dict[key])
#     except RuntimeError as e:
#         print(e)

# 上面两种方法均会出现RuntimeError异常错误，改良后的代码如下
for key in list(globals_dict.keys()):
    print(key, globals_dict.get(key, 'steverocket'))