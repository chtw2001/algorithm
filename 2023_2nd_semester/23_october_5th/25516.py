import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
tree = [[] for _ in range(N)]
visited = [0]*N

for _ in range(N-1):
    p, c = map(int, input().split())
    tree[p].append(c)

q = deque()
q.append((0, 0)) # parent, floor
apple = list(map(int, input().split()))

answ = 0
while q:
    parent, floor = q.popleft()
    if floor > K:
        break
    if apple[parent]:
        answ += 1
        
    visited[parent] = 1
    for i in tree[parent]:
        if not visited[i]:
            q.append((i, floor+1))
            visited[i] = 1

print(answ)