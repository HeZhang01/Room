import threading

"""
排它锁
lock =threading.Lock()
"""

"""重入锁  """
lock = threading.RLock()

def something1():
    with lock:
        print('Lock acquire in something1')
    print('Lock release in something1')

    return 'Done something1'

def something2():

    with lock:
        print('Lock acquire in something2')
    print('Lock release in something2')

    return 'Done something2'

def main():
    with lock:
        result1 = something1();
        result2 = something2();
    print(result1)
    print(result2)

if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(target=main)
        my_thread.start()
