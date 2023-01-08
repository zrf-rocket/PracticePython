# -*- encoding:utf-8 -*-

__AUTHOR__ = "zhouruifu"
__TIME__ = "2018/09/15"
__VERSION__ = 1.0

import time

def decorator_times(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print u"总运行时间：{:.3f}秒".format(end - start)
    return wrapper
