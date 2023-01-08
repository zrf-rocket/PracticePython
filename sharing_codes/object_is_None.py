# -*- encoding:utf-8 -*-

__AUTHOR__ = "zhouruifu"
__TIME__ = "2018/09/15"
__VERSION__ = 1.0


print [] == None
print False == None
print "" == False

#判断集合是否为空
non_contents = {}

if non_contents is not None:
    print "Yes"
else: #@TODO 此处else分支永远也不会被执行到
    print "No"


#规范写法
if non_contents:
    print "Yes"
else:
    print "No"