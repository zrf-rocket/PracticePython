#-*- encoding:utf-8 -*-
# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，还有多重继承、定制类、元类
# 定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性

class Object(object):
    pass

#该对象绑定一个属性和方法
o = Object()
o2 = Object()
o.name = "object"
print o.name

#该实例绑定一个方法
def set_age(self,age): #定义一个函数作为实例方法
    self.age = age

from types import MethodType
o.set_age = MethodType(set_age,o) #给实例绑定一个方法
#调用实例方法
o.set_age(25)
print o.age

#给实例绑定的方法  对另一个实例并不起作用
# o2.set_age(24)


def set_score(self,score):
    self.score = score
#只有给class绑定的方法，才会对所有的实例起作用
Object.set_score = set_score
o.set_score(100)
print o.score

o2.set_score(200)
print o2.score

# 上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。


# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ("name","age") #用tuple定义允许绑定的属性名称

s = Student()
s.name = "names"
s.age = "ages"
# s.score = "scores"  #AttributeError: 'Student' object has no attribute 'score'
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9000  #ok


# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
