# https://www.jianshu.com/p/b5e347b3a17c

import time
import asyncio


def now():
    return time.time()


async def do_some_work(x):
    print('2- Waiting: ', x)

start = now()

coroutine = do_some_work(2)
print('1-', coroutine)
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)  # encapsulate coroutine to Task automatically

print('TIME: ', now() - start)

