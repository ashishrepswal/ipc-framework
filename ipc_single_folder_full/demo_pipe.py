#!/usr/bin/env python3
from ipc_pipe import IPCPipe

if __name__ == '__main__':
    ipc = IPCPipe()
    try:
        r, w = ipc.create()
        ipc.write(w, 'Hello through pipe')
        print('Read:', ipc.read(r))
    except Exception as e:
        print(f"[ERROR] Pipe demo failed: {e}")
