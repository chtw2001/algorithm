# 5번 스트레이트 스위치 게임

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
status = list(map(int, input().split()))
dice = [list(map(int, input().split()))[1:] for _ in range(K)]

ex = 0
for i in range(N):
    ex = ex*5 + 4 # 가장 큰 수는 4, 가능한 최대 hash => ex

cache = [-1]*(ex+1)

def makeHash(status):
    hash = 0
    for i in range(N):
        hash = (hash*5) + status[i]
    
    return hash

def cal(status, switch):
    for idx in dice[switch]:
        status[idx-1] = (status[idx-1] + switch+1) % 5

q = deque()
q.append((status))
cache[makeHash(status)] = 0
while q:
    state = q.popleft()
    hash = makeHash(state)
    for i in range(K):
        state_ = state.copy()
        cal(state_, i)
        hash_ = makeHash(state_)
        if cache[hash_] != -1:
            continue
        cache[hash_] = cache[hash] + 1
        q.append(state_)

answ = sys.maxsize
for j in range(5):
    ex = 0
    for _ in range(N):
        ex = ex*5 + j
    if cache[ex] == -1:
        continue
    else:
        answ = min(answ, cache[ex])
        
if answ == sys.maxsize:
    print(-1)
else:
    print(answ)