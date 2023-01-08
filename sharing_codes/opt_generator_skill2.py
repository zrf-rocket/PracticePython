#-*- encoding:utf-8 -*-
def series():
    num1 = 10
    num2 = 20
    #@TODO 生成器此处的循环不会造成死循环
    while True:
        yield num1 + num2
        num1 += 1
        num2 += 1
        print "In the end"

gen = series()
print gen.next()#执行完之后挂起
print gen.next()#再次调用恢复现场
# print gen.next()
