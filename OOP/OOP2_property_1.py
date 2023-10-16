#-*- encoding:utf-8 -*-
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
# 显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，
# 这样，在set_score()方法里，就可以检查参数

class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must ba an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0~100")
        self._score = value

s = Student()
s.set_score(90)
print s.get_score()


# 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了
# s.set_score(109)
s.set_score(-0)
# s.set_score(-1)


# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
# 装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must ba an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0~100")
        self._score = value
# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作

s2 = Student2()
s2.score = 50
print s2.score
# s2.score = 900

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Student3(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2017-self._birth
# birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    #可读可写的width
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        #严谨性判断
        if not isinstance(value,(int,float)):
            raise ValueError("width must be a number")
        if value <= 0:
            raise ValueError("width must be bigger than 0")
        self._width = value

    # 可读可写的height
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        #这种重复性的相同属性判断功能  还可以放入到装饰器中
        if not isinstance(value,(int,float)):
            raise ValueError("width must be a number")
        if value <= 0:
            raise ValueError("width must be bigger than 0")
        self._height = value

    #只读属性的resolution
    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 789
print s.resolution
assert s.resolution == 807937,"1024 * 789 = %d ?" % s.resolution