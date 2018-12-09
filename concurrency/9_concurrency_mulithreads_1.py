from threading import Thread
import time
import asyncio

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))


new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()

new_loop.call_soon_threadsafe(more_work, 4)
new_loop.call_soon_threadsafe(more_work, 2)  # took 6s
print("main thread is not blocked")
