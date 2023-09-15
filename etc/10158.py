import sys
input = sys.stdin.readline
C, R = map(int, input().split())
k = int(input())
ori_R = R
if k > C*R:
    print(0)
    quit()
if k == 1:
    print(1, 1)
    quit()

cnt = 1
xy = [1, 1]

def plus_R():
    global R, cnt, xy
    for _ in range(R-1):
        xy[1] += 1
        cnt += 1
        if k == cnt:
            return xy
    R -= 1

def plus_C():
    global C, cnt, xy
    for _ in range(C-1):
        xy[0] += 1
        cnt += 1
        if k == cnt:
            return xy
    C -= 1

def minus_R():
    global R, cnt, xy
    for _ in range(R-1):
        xy[1] -= 1
        cnt += 1
        if k == cnt:
            return xy
    R -= 1

def minus_C():
    global C, cnt, xy
    for _ in range(C-1):
        xy[0] -= 1
        cnt += 1
        if k == cnt:
            return xy
    C -= 1

answ = 0

while True:
    answ = plus_R()
    if ori_R-1 == R:
        R += 1
        ori_R = -10
    if answ != None:
        print(xy[0], xy[1])
        quit()

    answ = plus_C()
    if answ != None:
        print(xy[0], xy[1])
        quit()

    answ = minus_R()
    if answ != None:
        print(xy[0], xy[1])
        quit()

    answ = minus_C()
    if answ != None:
        print(xy[0], xy[1])
        quit()