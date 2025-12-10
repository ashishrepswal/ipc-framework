#!/usr/bin/env python3
from ipc_queue import IPCQueue

if __name__ == '__main__':
    q = IPCQueue()
    q.push('Hello queue')
    print('Popped:', q.pop())
