import time
from multiprocessing.managers import BaseManager
import asyncio
from threading import Thread


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_sleep(x, queue):
    await asyncio.sleep(x)
    queue.put(str(x) + " is done")
    print(x, " is done")


def consumer():
    while True:
        task = task_queue.get()
        if not task:
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_sleep(int(task), result_queue), new_loop)


BaseManager.register('get_task_queue')
BaseManager.register('get_result_queue')

server_addr = '192.168.1.100'
print('connect to server %s...' %server_addr)

manager = BaseManager(address=(server_addr, 20000), authkey=b'abc')
manager.connect()
task_queue = manager.get_task_queue()
result_queue = manager.get_result_queue()

print(time.ctime())
new_loop = asyncio.new_event_loop()

loop_thread = Thread(target=start_loop, args=(new_loop,))
loop_thread.setDaemon(True)
loop_thread.start()


consumer_thread = Thread(target=consumer)
consumer_thread.setDaemon(True)
consumer_thread.start()

while True:
    time.sleep(0.1)