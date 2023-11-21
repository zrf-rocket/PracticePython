# slice()函数的使用示例
# 创建切片对象
# 一个参数
s1 = slice(5)
# 两个参数
s2 = slice(1, 2)
# 三个参数
s3 = slice(2, 5, 2)

# 切片操作
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[s1])  # 输出：[1, 2, 3, 4, 5]
print(lst[s2])  # 输出：[2]
print(lst[s3])  # [3, 5]