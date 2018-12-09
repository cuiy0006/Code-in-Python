import time
from multiprocessing.managers import BaseManager
import asyncio
import threading
from threading import Thread
import aiohttp


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            return await resp.text()


async def do_some_work(url):
    print('waiting...', url)
    print('current thread:', threading.current_thread())
    try:
        ret = await fetch(url)
        result_queue.put(ret)
    except Exception as e:
        print(e)
    else:
        print('{} ... done'.format(url))

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

while True:
    task = task_queue.get()
    if not task:
        time.sleep(1)
        continue
    asyncio.run_coroutine_threadsafe(do_some_work(task), new_loop)

