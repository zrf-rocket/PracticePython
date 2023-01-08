# -*- encoding:utf-8 -*-
import math


"""
循环语句的优化技巧
"""

number = 9

class Cycle(object):
    """
    循环内部计算提到外部
    优先采用局部变量
    """
    def calc1(self):
        number = 144
        sums = 0
        for item in range(100):
            res = math.sqrt(number)
            sums += item * res
        print sums

    def calc2(self):
        number = 144 #优先级最高
        sums = 0
        res = math.sqrt(number)
        for item in range(100):
            sums += item * res
        print sums

if __name__ == '__main__':
    cycle = Cycle()
    cycle.calc1()
    cycle.calc2()








