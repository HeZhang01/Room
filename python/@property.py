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

# print('myfunc is %s' % myfunc.__name__)
# myfunc = deco2(myfunc)  # myfunc 被改变
# print('myfunc is %s' % myfunc.__name__)
# print("\n")
# myfunc()


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# s = Student()
# s.score = 89
# print(s.score)


# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be integer')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 20
# s.width = ''
print('width is %d' % s.width)
s.height = 20
print('height is %d' % s.height)
print('resolution is %d' % s.resolution)
# s.resolution = 400