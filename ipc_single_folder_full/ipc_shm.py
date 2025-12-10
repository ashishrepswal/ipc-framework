#!/usr/bin/env python3
# ipc_shm.py
from multiprocessing import shared_memory
import sys

DEFAULT_SIZE = 1024

class SharedMemoryWriter:
    def __init__(self, size=DEFAULT_SIZE):
        self.size = size
        self.shm = shared_memory.SharedMemory(create=True, size=self.size)

    def write(self, text: str):
        data = text.encode()[:self.size]
        self.shm.buf[:len(data)] = data
        return self.shm.name

    def close(self):
        try:
            self.shm.close()
        except:
            pass

class SharedMemoryReader:
    def __init__(self, name, size=DEFAULT_SIZE):
        self.name = name
        self.size = size
        self.shm = shared_memory.SharedMemory(name=self.name)

    def read(self):
        raw = bytes(self.shm.buf[:self.size])
        return raw.rstrip(b"\x00").decode()

    def close(self):
        try:
            self.shm.close()
        except:
            pass

if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == 'write':
        text = ' '.join(sys.argv[2:]) or 'hello shm'
        w = SharedMemoryWriter()
        name = w.write(text)
        print(name)
        w.close()
    elif len(sys.argv) >= 3 and sys.argv[1] == 'read':
        name = sys.argv[2]
        r = SharedMemoryReader(name)
        print(r.read())
        r.close()
    else:
        print('Usage:')
        print('  python3 ipc_shm.py write <message>')
        print('  python3 ipc_shm.py read <shm_name>')
