#!/usr/bin/env python3
from ipc_shm import SharedMemoryWriter

if __name__ == '__main__':
    w = SharedMemoryWriter()
    name = w.write('Hello from SHM demo')
    print('Shared memory name (use this to read):', name)
    w.close()
