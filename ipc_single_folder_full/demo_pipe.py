#!/usr/bin/env python3
from ipc_pipe import IPCPipe

if __name__ == '__main__':
    ipc = IPCPipe()
    r, w = ipc.create()
    ipc.write(w, 'Hello through pipe')
    print('Read:', ipc.read(r))
