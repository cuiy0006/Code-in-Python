# not a good way

import time
from multiprocessing.managers import BaseManager
import asyncio
import aiohttp


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            return await resp.text()


async def worker(id):
    print('start worker')
    while True:
        url = task_queue.get()
        if not url:
            time.sleep(1)
            continue
        try:
            ret = await fetch(url)
            result_queue.put(ret)
        except Exception as e:
            print(e)
        else:
            print('{} ... done by work {}'.format(url, id))


BaseManager.register('get_task_queue')
BaseManager.register('get_result_queue')

server_addr = '192.168.1.100'
print('connect to server %s...' %server_addr)

manager = BaseManager(address=(server_addr, 20000), authkey=b'abc')
manager.connect()
task_queue = manager.get_task_queue()
result_queue = manager.get_result_queue()


asyncio.ensure_future(worker(1))
asyncio.ensure_future(worker(2))

loop = asyncio.get_event_loop()
try:
    loop.run_forever()
except KeyboardInterrupt as e:
    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()




