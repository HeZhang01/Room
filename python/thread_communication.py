import threading

from queue import Queue

"""
基于Queue的线程通信

"""

def creator(data, q):
    """
    生成用于消费的数据，等待消费者完成处理
    
    """

    print('Creating data and putting it on the queue')
    for item in data:
        evt = threading.Event()
        q.put( (item, evt) )

        print('Waiting for data to be doubled')
        evt.wait()

    end_flag = '#a.1Q%$4'
    evt = threading.Event()
    q.put( (end_flag, evt) )
    print('Waiting for end')
    evt.wait


def consumer(q):
    """
    消费部分数据，并做处理（将输入翻一倍）
    
    """
    while True:
        data, evt = q.get()
        if data == '#a.1Q%$4':
            print('end......')
            break
        print('data found to be processed: {}'.format(data))
        processed = data * 2
        print(processed)
        evt.set()
        q.task_done()

if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]
    thread1 = threading.Thread(target=creator, args=(data,q))
    thread2 = threading.Thread(target=consumer, args=(q,))

    thread1.start()
    thread2.start()

    q.join()

