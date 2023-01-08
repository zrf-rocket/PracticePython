# -*- encoding:utf-8 -*-

__AUTHOR__ = "zhouruifu"
__TIME__ = "2018/09/15"
__VERSION__ = 1.0



from decorator_times import decorator_times

"""
针对字符串的连接：join与+的性能对比
"""

# times = 10000
# times = 100000
times = 1000000
str_list = ["this is Pythonic" for item in range(times)]

@decorator_times
def test_join():
    return "".join(str_list)

@decorator_times
def test_plus():
    result = ""
    for _, value in enumerate(str_list):
        result += value
    return result

if __name__ == '__main__':
    test_join()
    test_plus()
