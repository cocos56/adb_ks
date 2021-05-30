from time import sleep
from random import randint
from os import system
from datetime import datetime

sd = datetime.now()

cmds = ['adb.exe -s cf27d741 tcpip 5555',
        'adb.exe disconnect 192.168.1.22:5555',
        'adb.exe connect 192.168.1.22:5555']
for c in cmds:
    system(c)

cmds = ['adb.exe -s b4e0becc tcpip 5555',
        'adb.exe disconnect 192.168.1.24:5555',
        'adb.exe connect 192.168.1.24:5555']
for c in cmds:
    print(c)
    system(c)


def run(device):
    r = randint(6, 30)
    x1 = randint(200, 700)
    y1 = randint(1200, 1350)
    x2 = randint(200, 700)
    y2 = randint(200, 500)
    cmd = 'adb.exe -s %s shell input swipe %d %d %d %d' % (device, x1, y1, x2, y2)
    print(cmd)
    system(cmd)
    print("随机休息", r, '秒', sep='')
    print('已运行：', datetime.now() - sd, sep='', end='\n\n')
    return r


r1 = r2 = 0

while True:
    if r1 <= 0:
        r1 = run('192.168.1.22:5555')
    if r2 <= 0:
        r2 = run('192.168.1.24:5555')
    r1 -= 3
    r2 -= 3
    sleep(3)
