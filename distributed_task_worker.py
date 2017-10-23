import time, sys, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

def test():
    server_addr = '192.168.1.3'
    print('connect to server %s...' %server_addr)

    manager = QueueManager(address=(server_addr, 20000), authkey=b'abc')
    manager.connect()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        try:
            n = task.get(timeout = 1)
            print('run task %d * %d' %(n, n))
            r = '%d * %d = %d' %(n, n, n*n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is Empty')

    print('worker exist.')

if __name__ == '__main__':
    freeze_support()
    test()
