import asyncio

import time


def now():
    return time.time()


async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(2)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    dones, pendings = await asyncio.wait(tasks)
    for task in dones:
        print("Task ret:", task.result())

start = now()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())

    print('-----------------------------')
    print(asyncio.gather(*asyncio.Task.all_tasks()))  # <_GatheringFuture pending>
    print(asyncio.wait(asyncio.Task.all_tasks()))  # <coroutine object wait at 0x00000260C6E15B48>
    print('-----------------------------')
    print(asyncio.gather(*asyncio.Task.all_tasks()).__class__.mro())
    print(asyncio.wait(asyncio.Task.all_tasks()).__class__.mro())

    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print('TIME: ', now() - start)