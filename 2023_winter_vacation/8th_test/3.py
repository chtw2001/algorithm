# 3번
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
ary = dict()
start_ary = [0]*(N+1)

for i in range(1, N):
    num = int(input())
    ary[i] = list(map(int, input().split()))
    for node in ary[i]:
        start_ary[node] = i

q = deque()
visited = [0]*(N+1)
q.append(1)
while q:
    node = q.popleft()
    if node == N:
        continue
    if visited[node]:
        print('CYCLE')
        quit()
    visited[node] = 1
    for child in ary[node]:
        q.append(child)
    
print('NO CYCLE')
