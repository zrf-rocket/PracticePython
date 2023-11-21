from inner_module_def_datastruct import WEIXIN_URL
# locals()函数的使用示例
def my_func():
    blog = WEIXIN_URL
    name = 'SteveRocket'
    age = 18
    print(locals())

my_func()  # 输出：{'blog': 'https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q', 'name': 'SteveRocket', 'age': 18}

# 用在此处locals与globals的输出结果一样
print(locals())
print(globals())



def my_func():
    x = 1
    print(locals())  # {'x': 1}
    print(globals())  # {...} 全局作用域的字典

my_func()
