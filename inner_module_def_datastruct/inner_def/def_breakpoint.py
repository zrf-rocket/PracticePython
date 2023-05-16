from inner_module_def_datastruct.inner_def import WEIXIN_URL

# breakpoint()函数的使用示例
def func(a, b):
    c = a + b
    print(WEIXIN_URL)
    breakpoint()  # 在此处设置断点
    return c

x = 1
y = 2
z = func(x, y)
print(z)