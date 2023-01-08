#-*- encoding:utf-8 -*-
import gc

class PyMemIncrease(object):
    def __init__(self):
        print "this is class __init__ functions: id{}".format(id(self))


while True:
    # collected = gc.collect()
    obj1 = PyMemIncrease()
    obj2 = PyMemIncrease()

    print gc.garbage
    obj1.obj_name1 = obj2
    print gc.garbage
    obj2.obj_name2 = obj1

    # obj1 = None
    # obj2 = None
    # collected = gc.collect()
    print gc.garbage


