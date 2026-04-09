import sys
from collections import deque
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

N, m = map(int, input().split())
belif = [[] for _ in range(N+1)]
for _ in range(m):
    a, b = map(int, input().split())
    belif[b].append(a)
    
def check(n):
    q = deque()
    q.append(n)
    visited = [0]*(N+1)
    visited[n] = 1
    cnt = 0
    while q:
        a = q.popleft()
        for i in belif[a]:
            if not visited[i]:
                q.append(i)
                cnt += 1
                visited[i] = 1
    return cnt
                
queue = []
for i in range(1, N+1):
    push(queue, (-check(i), i))

while queue:
    ex = pop(queue)
    print(ex[1], end=' ')
    if not queue or ex[0] != queue[0][0]:
        break