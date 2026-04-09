import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

X = int(input())
dict = dict()
N = int(input())
set = []
for _ in range(N):
    person, point = map(str, input().split())
    point = float(point)
    if point/X*100 < 5:
        continue
    for i in range(1, 15):
        push(set, (-point/i, person))
    dict[person] = 0

for i in range(14):
    point, person = pop(set)
    dict[person] += 1

for key in sorted(dict.keys()):
    print(key, dict[key])
