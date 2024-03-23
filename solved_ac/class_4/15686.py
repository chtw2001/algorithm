# 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
house = []
chickin = []
for i in range(N):
    ex = list(map(int, input().split()))
    for j in range(N):
        if ex[j] == 1:
            house.append((i, j))
        elif ex[j] == 2:
            chickin.append((i, j))

answ = sys.maxsize
for comb in combinations(chickin, M):
    total = 0 # chickin street from all house
    for i, j in house: 
        min_ex = sys.maxsize
        for x, y in comb:
            ex = abs(i-x) + abs(j-y)
            min_ex = min(min_ex, ex)
        total += min_ex
    answ = min(answ, total)

print(answ)
