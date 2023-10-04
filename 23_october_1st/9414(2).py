import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

TC = int(input())
while TC > 0:
    money = 5*pow(10, 6)
    q = []
    while True:
        ex = int(input())
        if not ex:
            break
        push(q, -ex) # max heap
    
    t = 1
    flag = 0
    answ = 0
    while q:
        answ += 2*pow(-pop(q), t)
        if answ > money:
            print('Too expensive')
            flag = 1
            break
        t += 1
    
    if not flag:
        print(answ)

    TC -= 1
