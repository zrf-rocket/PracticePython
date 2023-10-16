# @author:SteveRocket 
# @Date:2023/4/23
# @File:random_demo1
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
import string, random, secrets
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)

# 随机生成一个字母
# 这 random.choice() 函数用于从指定的序列中选择一个随机项。这个想法是使用 ascii_letters 从常数 string 模块，它返回一个包含范围的字符串 A-Za-z，即小写和大写字母。
print(random.choice(string.ascii_letters))
# 如果您需要生成加密安全的随机字母，请考虑使用 choice() 从函数 secrets 模块。
print(secrets.choice(string.ascii_letters))

# 这 random.randint(x, y) 函数生成随机整数 n 这样 x <= n <= y.如果您需要生成一个随机字母
def randletter(x, y):
    return chr(random.randint(ord(x), ord(y)))

# 在 `a-z` 范围内生成一个随机字母
print(randletter('a', 'z'))
# 在`A-Z`范围内生成一个随机字母
print(randletter('A', 'Z'))

#随机选择字母`r`或`R`
rand = ('r', 'R')[random.randint(0, 1)]
print(rand)


while 1:
    pwd = ""
    for i in range(4):
        pwd += random.choice(string.ascii_letters)
    print(pwd)



