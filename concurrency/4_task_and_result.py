import time
import asyncio


def now():
    return time.time()


async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print('result:', task.result())
print('TIME: ', now() - start)