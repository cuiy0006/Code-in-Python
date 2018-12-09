import asyncio
import time


def now():
    return time.time()


async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)  # await a corountine
    return 'Done after {}s'.format(x)

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
print(task.__class__.mro())
loop.run_until_complete(task)

print('Task ret: ', task.result())
print('TIME: ', now() - start)

