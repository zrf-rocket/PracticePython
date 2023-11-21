# id()函数的使用示例
# 获取整数、字符串、列表、字典的地址
a = 10
print(id(a))  # 140727023900624

b = "hello"
print(id(b))  # 140727023997936

c = [1, 2, 3]
print(id(c))  # 140727023999872

d = {"name": "Alice", "age": 18}
print(id(d))  # 140727024000000

# 不可变类型示例
e = "world"
f = "world"
print(id(e))  # 140727023999856
print(id(f))  # 140727023999856
print(id(e) == id(f))  # True

# 可变类型示例
g = [1, 2, 3]
h = [1, 2, 3]
print(id(g))  # 140727023998080
print(id(h))  # 140727023998208
