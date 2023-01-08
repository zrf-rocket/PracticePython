# -*- encoding:utf-8 -*-

"""
使用生成器提高效率
"""

def use_generator():
    for item in range(10):
        yield item*2

gen_obj = use_generator()
print type(gen_obj),gen_obj

# 获取迭代对象中的内容
print gen_obj.next()
print

#对可迭代的对象进行遍历
for item in gen_obj:
    print item
