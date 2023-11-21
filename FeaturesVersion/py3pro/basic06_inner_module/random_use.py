# 方法1：生成随机数

import random

# 生成一个随机整数
print("随机整数：", random.randint(0, 10))


# 随机生成实数  下面生成的实数符合均匀分布(uniform distribution)，意味着某个范围内的每个数字出现的概率相等
# 生成一个随机浮点数
print("随机浮点数：", random.uniform(0, 10))  # 随机生成下一个实数，它在[a,b]范围内。

# 生成一个随机实数（可以是无限精度的实数）  随机生成下一个实数，它在[0,1)范围内。
print("随机实数：", random.random())


# 方法2：打乱序列

import random

arr = [1, 2, 3, 4, 5]
print(random.shuffle(arr))  # 返回None
print("随机打乱序列：", arr)  # 将序列的所有元素随机排序


# 方法3：随机选择元素
import random

# 从序列的元素中随机挑选一个元素
arr = [1, 2, 3, 4, 5]
print("随机选择元素：", random.choice(arr))

# 从列表中随机取出3个元素
from random import sample
li = ["123", 456, False, 'steverocket']
print(sample(li, 3))

# 从列表中随机取出5个字符
from inner_module_def_datastruct import WEIXIN_URL
print(sample(WEIXIN_URL, 5))



# 方法4：生成正态分布数据

from random import normalvariate

# 生成一个平均值为0，标准差为1的正态分布数据
print("正态分布数据：", normalvariate(0, 1))
print("正态分布数据：", normalvariate(1, 10)) # 正态分布


from random import seed
print(seed(100))  # 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。


# 方法5：高斯分布
from random import gauss, expovariate
# gauss(mu,sigma)    # 随机生成符合高斯分布的随机数，mu,sigma为高斯分布的两个参数。
print(gauss(1, 10))
# 多线程注意事项：当两个线程同时调用此方法时，它们有可能将获得相同的返回值。 这可以通过三种办法来避免。
# 1) 让每个线程使用不同的随机数生成器实例。
# 2) 在所有调用外面加锁。
# 3) 改用速度较慢但是线程安全的 normalvariate() 函数。



# 方法6：指数分布
# expovariate(lambd) # 随机生成符合指数分布的随机数，lambd为指数分布的参数。
print(expovariate(1 / 5))
#  lambd 是 1.0 除以所需的平均值，它应该是非零的。 （该参数本应命名为 “lambda” ，但这是 Python 中的保留字。）如果 lambd 为正，则返回值的范围为 0 到正无穷大；如果 lambd 为负，则返回值从负无穷大到 0。



# 方法7：对数状态分布
from random import lognormvariate
# lognormvariate(mu, sigma) 对数正态分布。 如果你采用这个分布的自然对数，你将得到一个正态分布，平均值为 mu 和标准差为 sigma 。 mu 可以是任何值，sigma 必须大于零。
print(lognormvariate(1.5, 1))


# 方法8：Pareto分布（帕累托分布）、Weibull分布（威布尔分布）
from random import paretovariate, weibullvariate
print(paretovariate(1.5))  # alpha 是形状参数。
print(weibullvariate(1.5, 1))  # alpha 是比例参数，beta 是形状参数。
