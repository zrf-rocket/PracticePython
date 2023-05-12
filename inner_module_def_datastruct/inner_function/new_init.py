# __new__方法是真正的类构造方法，用于产生实例化对象（空属性）。重写__new__方法可以控制对象的产生过程。
# __init__方法是初始化方法，负责对实例化对象进行属性值初始化，此方法必须返回None，__new__方法必须返回一个对象。重写__init__方法可以控制对象的初始化过程。

# 使用new来处理单例模式
class Student:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def speek(self):
        print("this is python3.11")


stu1 = Student()
stu2 = Student()
print(id(stu1), id(stu2))  # 输出ID相同：2759258052624 2759258052624
print(stu1 is stu2) # True
# __new__一般很少用于普通的业务场景，更多的用于元类之中，因为可以更底层的处理对象的产生过程。而__init__的使用场景更多。