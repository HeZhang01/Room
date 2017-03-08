"""
装饰器
"""
import time


# 一个简单的需求： 得到一个函数的大致执行时间

def deco(func):
    startTime = time.time()
    func()
    endTime = time.time()
    msecs = (endTime - startTime) * 1000
    print('spend time: %f ms' % msecs)


def myfunc():
    print('start myfunc')
    time.sleep(0.6)
    print('end myfunc')


# deco(myfunc)
# myfunc()

# 一个问题 每次调用myfunc函数的时候都要用deco(myfunc)代替 myfunc->deco(myfunc)

def deco2(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print('spend time: %f ms' % msecs)
    return wrapper

print('myfunc is %s' % myfunc.__name__)
myfunc = deco2(myfunc)  # myfunc 被改变
print('myfunc is %s' % myfunc.__name__)
print("\n")
myfunc()

