# 方法1：获取当前日期和时间

import datetime

# 获取当前日期和时间
now = datetime.datetime.now()
print("当前日期和时间:", now)

# 方法2：格式化日期和时间

import datetime

# 格式化日期和时间
now = datetime.datetime.now()
print("当前日期和时间:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 方法3：时间间隔计算

import datetime

# 计算两个日期之间的天数
d1 = datetime.date(2022, 6, 1)
d2 = datetime.date(2022, 6, 10)
delta = d2 - d1
print("相差的天数:", delta.days)

# 方法4：时区转换

import datetime
from dateutil import tz

# 转换时区
utc_time = datetime.datetime.utcnow()
print('UTC时间:', utc_time)
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Asia/Shanghai')
local_time = utc_time.replace(tzinfo=from_zone).astimezone(to_zone)
print('转换后的本地时间:', local_time)


# 时间类型
import datetime
print(datetime.date)  # <class 'datetime.date'>
print(datetime.time)   # <class 'datetime.time'>
print(datetime.datetime)   # <class 'datetime.datetime'>

dt = datetime.datetime(2022, 9, 13, 21, 37)
print(dt, type(dt)) # 2022-09-12 21:37:00 <class 'datetime.datetime'>
print(dt.year, dt.month, dt.day, dt.weekday(), dt.hour, dt.minute, dt.second, dt.microsecond) # 2022 9 13 1 21 37 0 0



# 时间运算和比较
# datetime包还定义了时间间隔对象(timedelta)。一个时间点(datetime)加上一个时间间隔(timedelta)可以得到一个新的时间点(datetime)。
import datetime
#
# t = datetime.datetime(2023, 9, 3, 21, 30)
t_next = datetime.datetime(2023, 9, 5, 23,30)
# # 下面的参数还可以是：days, hours, milliseconds, microseconds
# delta1 = datetime.timedelta(seconds = 600)
# delta2 = datetime.timedelta(weeks = 3)
# print(t + delta1) # 2023-09-03 21:40:00
# print(t + delta2) # 2023-09-24 21:30:00
# print(t_next - t) # 2 days, 2:00:00
# print(t, t_next) # 2023-09-03 21:30:00 2023-09-05 23:30:00
# # 时间的比较
# print(t > t_next) # False


# datetime对象与字符串转换
from datetime import datetime
format = "output-%Y-%m-%d-%H%M%S.txt"
str    = "output-2023-6-15-220000.txt"
t      = datetime.strptime(str, format)
print(t, type(t))  # 2023-06-15 22:00:00   <class 'datetime.datetime'>


print(t_next.strftime(format))  # output-2023-09-05-233000.txt
