import os
from time import sleep

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('-=' * 40)
        os.system(f'ping -n 6 {ip}')
        print('-=' * 40)
        sleep(5)
