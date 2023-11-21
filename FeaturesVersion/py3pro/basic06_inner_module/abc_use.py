from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        # 抽象方法是一种没有实现的方法
        pass

class Dog(Animal):
    def eat(self):
        print('Dog eat meat.')

class Cat(Animal):
    def eat(self):
        print('Cat eat fish.')

class Rat(Animal):
    pass



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

if __name__ == '__main__':
    # d = Dog()
    # d.eat()
    # c = Cat()
    # c.eat()
    # r = Rat()
    # r.eat()  # TypeError: Can't instantiate abstract class Mouse with abstract methods eat



    r = Rectangle(5, 3)
    print(r.area())  # 15
    print(r.perimeter())  # 16

    c = Circle(2)
    print(c.area())  # 12.56
    print(c.perimeter())  # 12.56
