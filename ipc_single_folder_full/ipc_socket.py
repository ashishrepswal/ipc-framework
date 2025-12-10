#!/usr/bin/env python3
# ipc_socket.py
# Simple UNIX domain socket server/client that works on macOS and Linux.
import socket
import os
import sys

SOCK_PATH = "/tmp/ipc_framework.sock"

class IPCSocketServer:
    def __init__(self, sock_path=SOCK_PATH):
        self.sock_path = sock_path
        if os.path.exists(self.sock_path):
            try:
                os.remove(self.sock_path)
            except Exception:
                pass
        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.s.bind(self.sock_path)
        os.chmod(self.sock_path, 0o600)
        self.s.listen(5)

    def start(self):
        print("Socket server started at", self.sock_path)
        try:
            while True:
                conn, _ = self.s.accept()
                uid = None
                # Try multiple methods to get peer uid (portable)
                try:
                    # Linux: SO_PEERCRED
                    import struct, socket as _sock
                    creds = conn.getsockopt(_sock.SOL_SOCKET, _sock.SO_PEERCRED, 12)
                    pid, uid, gid = struct.unpack('3i', creds)
                except Exception:
                    try:
                        # macOS: getpeereid
                        uid, gid = socket.getpeereid(conn.fileno())
                    except Exception:
                        uid = os.geteuid()
                print("[AUTH] Connection from UID =", uid)
                data = conn.recv(4096)
                if data:
                    print("[RECV]", data.decode(errors='ignore'))
                    conn.sendall(b"ACK:" + data)
                conn.close()
        except KeyboardInterrupt:
            print("Server exiting")
        finally:
            try:
                self.s.close()
            except:
                pass
            try:
                if os.path.exists(self.sock_path):
                    os.remove(self.sock_path)
            except:
                pass

class IPCSocketClient:
    def __init__(self, sock_path=SOCK_PATH):
        self.sock_path = sock_path

    def send(self, msg: bytes):
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(self.sock_path)
        s.sendall(msg)
        resp = s.recv(4096)
        s.close()
        return resp

if __name__ == '__main__':
    # allow running as server or client for convenience
    if len(sys.argv) > 1 and sys.argv[1] == 'server':
        IPCSocketServer().start()
    elif len(sys.argv) > 1 and sys.argv[1] == 'client':
        msg = b' '.join([arg.encode() for arg in sys.argv[2:]]) or b'hello'
        print("Response:", IPCSocketClient().send(msg))
    else:
        print("Usage: python3 ipc_socket.py server|client [message]")
