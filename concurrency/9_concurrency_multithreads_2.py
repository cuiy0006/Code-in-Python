from threading import Thread
import asyncio


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_some_work(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))

new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()

asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(2), new_loop)  # took 4s
print("main thread is not blocked")
