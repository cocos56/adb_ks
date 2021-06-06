from time import sleep
from random import randint
from os import system
from datetime import datetime

sd = datetime.now()


def runCmds(device, ip):
    cmds = ['adb -s %s tcpip 5555' % device,
            'adb disconnect %s:5555' % ip,
            'adb connect %s:5555' % ip,
            'adb -s %s shell input keyevent 3' % ip,
            'adb -s %s shell input keyevent 82' % ip,
            'adb -s %s shell input tap 540 1706' % ip,
            'adb -s %s shell am start -n com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity' % ip,
            'adb -s %s shell input tap 519 1415' % ip
            ]
    for c in cmds:
        print(c)
        system(c)
        sleep(1)


runCmds('aa22a023', '192.168.1.27')
runCmds('25abcba8', '192.168.1.23')
runCmds('f8609940', '192.168.1.28')

sleep(9)


def run(device):
    r = randint(6, 30)
    x1 = randint(200, 700)
    y1 = randint(1363, 1477)
    x2 = randint(200, 700)
    y2 = randint(552, 709)
    cmd = 'adb.exe -s %s shell input swipe %d %d %d %d' % (device, x1, y1, x2, y2)
    print(cmd)
    system(cmd)
    print("随机休息", r, '秒', sep='')
    print('已运行：', datetime.now() - sd, sep='', end='\n\n')
    return r


r1 = r2 = r3 = 0

while True:
    if r1 <= 0:
        r1 = run('192.168.1.27:5555')
    if r2 <= 0:
        r2 = run('192.168.1.23:5555')
    if r3 <= 0:
        r3 = run('192.168.1.23:5555')
    r1 -= 3
    r2 -= 3
    r3 -= 3
    sleep(3)
