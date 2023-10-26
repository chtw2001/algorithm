import sys, math
from collections import defaultdict, deque
from heapq import heappush as push, heappop as pop
import turtle, datetime

for i in range(6):
    for j in range(6):
        print("*", end='')
    print()
print()

for i in range(6):
    for j in range(i+1):
        print("*", end='')
    print()
print()

for i in range(6):
    for j in range(6-i):
        print("*", end='')
    print()
print()

for i in range(6):
    for j in range(i):
        print(' ', end='')
    for j in range(6-i):
        print('*', end='')
    print()
print()

for i in range(6):
    for j in range(6-i):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    print()
print()

for i in range(6):
    for j in range(6-i-1):
        print(' ', end='')
    for j in range(i*2+1):
        print('*', end='')
    print()
print()