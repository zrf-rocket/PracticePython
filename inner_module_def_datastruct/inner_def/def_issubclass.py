# issubclass()函数的使用示例
class MyBaseClass:
    pass

class MySubClass(MyBaseClass):
    pass

class MyOtherClass:
    pass

print(issubclass(MySubClass, MyBaseClass))  # 输出：True
print(issubclass(MyOtherClass, MyBaseClass))  # 输出：False
print(issubclass(MySubClass, (MyBaseClass, MyOtherClass)))  # 输出：True
