#!/usr/bin/env python3
from ipc_shm import SharedMemoryReader
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        name = input('Enter shared memory name: ')
    else:
        name = sys.argv[1]
    r = SharedMemoryReader(name)
    print('Read:', r.read())
    r.close()
