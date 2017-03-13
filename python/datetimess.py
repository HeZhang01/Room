"""
datetime 练习
"""


# datetime timestamp str

from datetime import datetime
import time

now = datetime.now()
print(now)  # 2017-03-13 11:56:35.985122  年-月-日 时：分：秒.毫秒
print(type(now))  # <class 'datetime.datetime'> 类型为datetime

now = time.time()
print(now)
print(type(now))
print(datetime.fromtimestamp(now))

# timestamp                 => datetime                   (datetime.fromtimestamp())
# 1489378089.904357 (float) => 2017-03-13 12:08:09.904357 (datetime)

# timestamp => datetime
# time = datetime(2016, 3, 13, 12, 18)
time = 1489378089.904357
print(datetime.fromtimestamp(time))

# str       => datetime
time = datetime.strptime('2017-03-13 12:08:09', '%Y-%m-%d %H:%M:%S')
print(time)

# datetime => timestamp
time = datetime.now()
time = time.timestamp()  ##
print(time)
time = int(time)
print(datetime.fromtimestamp(time))

# TODO 具体应用的时候再参考


