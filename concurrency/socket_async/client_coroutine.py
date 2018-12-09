from __future__ import print_function
from selectors2 import DefaultSelector, EVENT_WRITE, EVENT_READ
import socket
from timeit import default_timer as timer


selector = DefaultSelector()
n_jobs = 0


class Future:
    def __init__(self):
        self.callbacks = []

    def resolve(self):
        callbacks = self.callbacks
        self.callbacks = []
        for fn in callbacks:
            fn()


class Task:
    def __init__(self, coro):
        self.coro = coro
        self.step()

    def step(self):
        try:
            next_future = next(self.coro)
        except StopIteration:
            return

        next_future.callbacks.append(self.step)


def get(path):
    global n_jobs
    n_jobs += 1
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', 5011))
    except socket.error:
        pass

    if path == '/foo':
        print('connecting<-foo')
    else:
        print('connecting<-bar')

    f = Future()
    file_no = s.fileno()
    selector.register(file_no, EVENT_WRITE, f)
    yield f
    selector.unregister(file_no)
    if path == '/foo':
        print('listening<-foo')
    else:
        print('listening<-bar')

    message = 'GET %s HTTP/1.0\r\n\r\n' % path
    s.send(message.encode('utf-8'))
    buf = []

    f = Future()
    selector.register(s.fileno(), EVENT_READ, f)

    while True:
        yield f
        chunk = s.recv(1000)
        if path == '/foo':
            print('reading<-foo')
        else:
            print('reading<-bar')
        if chunk:
            buf.append(chunk.decode('utf-8'))
        else:
            break

    selector.unregister(s.fileno())
    s.close()
    body = ''.join(buf)
    print(body)
    n_jobs -= 1


start = timer()
Task(get('/foo'))
Task(get('/bar'))
while n_jobs:
    events = selector.select()
    for key, mask in events:
        future = key.data
        future.resolve()

end = timer()
print(end - start)





