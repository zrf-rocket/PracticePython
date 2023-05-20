# reload()函数的使用示例
import math

# 修改my_module模块中的变量
math.x = 100

print(math.x) # 输出：100

# 使用reload()函数重新加载my_module模块
import importlib
importlib.reload(math)

# 输出修改后的变量值
print(math.x)  # 输出：100
