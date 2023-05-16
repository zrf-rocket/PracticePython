# str()函数的使用示例
# 将数字转换为字符串
n = 123
print(str(n))  # 输出：123

# 将列表转换为字符串
lst = [1, 2, 3]
print(str(lst))  # 输出：[1, 2, 3]

# 自定义对象的字符串表示形式
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"MyClass({self.x}, {self.y})"

obj = MyClass(1, 2)
print(str(obj))  # 输出：MyClass(1, 2)