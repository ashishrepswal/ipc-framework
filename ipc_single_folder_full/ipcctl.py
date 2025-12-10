#!/usr/bin/env python3
# ipcctl.py - tiny CLI stub for management
import argparse

parser = argparse.ArgumentParser(prog='ipcctl')
sub = parser.add_subparsers(dest='cmd')

p_create = sub.add_parser('create')
p_create.add_argument('--name', required=True)
p_create.add_argument('--backend', choices=['shm','socket','pipe','queue'], default='shm')

p_list = sub.add_parser('list')

args = parser.parse_args()

if args.cmd == 'create':
    print(f'Created channel {args.name} using backend {args.backend}')
elif args.cmd == 'list':
    print('channels: demo1, demo2')
else:
    parser.print_help()
