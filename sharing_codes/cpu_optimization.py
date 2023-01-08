# -*- encoding:utf-8 -*-

__AUTHOR__ = "zhouruifu"
__TIME__ = "2018/09/15"
__VERSION__ = 1.0



number_list = [1,2,3,4,5,6,7,8,9]

for item in number_list:
    if 1 == item:print True


for item in number_list:
    if 1 == item:
        print True
        break


print 1 in number_list
print 1 not in number_list