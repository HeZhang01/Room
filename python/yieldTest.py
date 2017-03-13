"""
yield 理解 练习
"""

# 可迭代对象
list = [1, 2, 3, 4]
print(list)
print(type(list))


for i in list:  # 可迭代对象(迭代器)可用for迭代生成
    print(i)

list = [x for x in range(4)]
print(list)
print(type(list))
for i in list:
    print(i)

for i in list:
    print(i)
  #  迭代器把所有值全部存储在内存中
  # 迭代是一个实现可迭代对象(实现的是 __iter__() 方法)和迭代器(实现的是 __next__() 方法)的过程。可迭代对象是你可以从其获取到一个迭代器的任一对象。迭代器是那些允许你迭代可迭代对象的对象

# 生成器
mygenerator = (x for x in range(4))
print(mygenerator)
print(type(mygenerator))

for i in mygenerator:
    print(i)

print('============')

for i in mygenerator:  # 在这里无法对生成器再次for in
    print(i)

mygenerator2 = mygenerator  # 复制生成器也是不可以再次使用for in
for i in mygenerator2:
    print(i)

  # 生成器是可以迭代的，但是你 只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时地生成数据

#  yield关键字
def createGenerator():
    list = range(4)
    for i in list:
        yield i

mygenerator = createGenerator()  # <generator object createGenerator at 0x7f46c40d16d0> 当你调用这个函数的时候，函数内部的代码并不立马执行 只是返回一个生成器对象
print(mygenerator)
for i in mygenerator:
    print(i)

# 一个协程的例子（消费者-生产者）
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
