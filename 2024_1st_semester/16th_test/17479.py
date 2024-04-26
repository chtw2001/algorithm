# 2번 

import sys
from collections import defaultdict
input = sys.stdin.readline
A, B, C = map(int, input().split())

normal = defaultdict(int)
for _ in range(A): # normal
    ex = list(map(str, input().split()))
    normal[ex[0]] = int(ex[1])

special = defaultdict(int)
for _ in range(B): # special
    ex = list(map(str, input().split()))
    special[ex[0]] = int(ex[1])

service = set()
for _ in range(C): # service
    service.add(input().rstrip())

normal_price, special_price, service_flag, special_flag = 0, 0, False, False

N = int(input())
for _ in range(N):
    menu = input().rstrip()
    if normal[menu]:
        normal_price += normal[menu]
    elif special[menu]:
        special_flag = True
        special_price += special[menu]
    else:
        if not service_flag:
            service_flag = True
        else:
            print("No")
            quit()


if special_flag:
    if normal_price < 20000:
        print("No")
        quit()
if service_flag:
    if normal_price + special_price < 50000:
        print("No")
        quit()

print("Okay")