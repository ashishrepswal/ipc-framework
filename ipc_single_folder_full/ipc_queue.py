#!/usr/bin/env python3
# ipc_queue.py - multiprocessing queue demo
import logging
logging.basicConfig(level=logging.INFO)
from multiprocessing import Queue

class IPCQueue:
    def __init__(self):
        self.q = Queue()

    def push(self, msg):
        self.q.put(msg)

    def pop(self):
        return self.q.get()

if __name__ == '__main__':
    q = IPCQueue()
    q.push('msg1')
   logging.info(f"Popped: {q.pop()}")
