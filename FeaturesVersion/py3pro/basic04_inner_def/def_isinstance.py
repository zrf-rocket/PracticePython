# isinstance()函数的使用示例
class MyClass:
    pass

a = 123
b = 'hello'
c = [1, 2, 3]
d = {'name': 'Tom', 'age': 18}
e = MyClass()

print(isinstance(a, int))  # 输出：True
print(isinstance(b, str))  # 输出：True
print(isinstance(c, (list, tuple)))  # 输出：True
print(isinstance(d, dict))  # 输出：True
print(isinstance(e, MyClass))  # 输出：True
print(isinstance(e, object))  # 输出：True