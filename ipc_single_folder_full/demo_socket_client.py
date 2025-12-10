#!/usr/bin/env python3
from ipc_socket import IPCSocketClient

if __name__ == '__main__':
    resp = IPCSocketClient().send(b'hello from client')
    print('Response:', resp)
