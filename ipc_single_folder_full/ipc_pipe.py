#!/usr/bin/env python3
# ipc_pipe.py - simple pipe demo
import os

class IPCPipe:
    def create(self):
        return os.pipe()

    def write(self, w, msg: str):
        if isinstance(msg, str):
            msg = msg.encode()
        os.write(w, msg)

    def read(self, r, n=1024):
        data = os.read(r, n)
        return data.decode()

if __name__ == '__main__':
    r,w = IPCPipe().create()
    IPCPipe().write(w, 'hello pipe')
    print('read from pipe:', IPCPipe().read(r))
