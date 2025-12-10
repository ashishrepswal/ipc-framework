# Python IPC Framework (Single-folder)

This is a simple **working** IPC framework demo in Python (single-folder layout) for macOS.
It includes examples for:
- UNIX domain sockets (server/client)
- Shared memory (writer/reader) using `multiprocessing.shared_memory`
- Pipes
- Multiprocessing Queue
- Simple ACL stub
- A tiny CLI stub

## Files in this folder
- ipc_socket.py              : Unix domain socket server/client
- ipc_shm.py                 : Shared memory writer/reader
- ipc_pipe.py                : Pipe example
- ipc_queue.py               : Multiprocessing Queue example
- acl.py                     : Simple ACL class
- ipcctl.py                  : Simple CLI stub
- demo_socket_server.py      : Runs the socket server
- demo_socket_client.py      : Runs the client that sends a message
- demo_shm_writer.py         : Writes message to shared memory and prints name
- demo_shm_reader.py         : Reads message from a given shared memory name
- demo_pipe.py               : Simple pipe demo (single-process)
- demo_queue.py              : Queue demo (single-process)
- requirements.txt
- .gitignore
- README.md

## Requirements
- Python 3.8+ (for multiprocessing.shared_memory)
- On macOS run with `python3` (example commands below)

## How to run examples (macOS)
Open Terminal and `cd` into this folder.

1. Socket server (keep running in one terminal)
```bash
python3 demo_socket_server.py
```

2. In another terminal, run the client:
```bash
python3 demo_socket_client.py
```

You should see the server print the received message and client print the ACK.

3. Shared memory writer (prints a name):
```bash
python3 demo_shm_writer.py
# copy printed name like 'psm_XXXX'
python3 demo_shm_reader.py
# when prompted, paste the name
```

4. Pipe demo:
```bash
python3 demo_pipe.py
```

5. Queue demo:
```bash
python3 demo_queue.py
```


## Project Overview
This repository contains a Python-based IPC (Inter-Process Communication) framework providing small demo modules for different IPC mechanisms. It is intended as an educational and reusable toolkit to demonstrate pipes, queues, shared memory, and socket-based IPC patterns.

## Features
- Demonstration of Pipes for direct process communication.
- Queue-based IPC examples using multiprocessing.
- Shared Memory reader/writer demos.
- Socket client-server examples for networked IPC.
- Small, well-documented demo scripts for quick testing.

## Quick Start
1. Clone the repo: `git clone https://github.com/ashishrepswal/ipc-framework.git`
2. Install requirements: `pip install -r requirements.txt`
3. Run demos from the `ipc_single_folder_full` directory, e.g.:
   - `python demo_pipe.py`
   - `python demo_queue.py`

