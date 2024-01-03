# 1번
import sys
from collections import defaultdict
input = sys.stdin.readline
N, K = map(int, input().split())

room = defaultdict(int)
for _ in range(N):
    S, Y = map(str, input().split())
    room[S+Y] += 1
    
answ = 0
for v in room.values():
    if v % K:
        answ += v // K + 1
    else:
        answ += v // K

print(answ)