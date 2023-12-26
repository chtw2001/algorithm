from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())

mapping = [0]*500000
visited = [0]*500000
move = [-1, 1]

for _ in range(M):
    s, e = map(int, input().split())
    try:
        mapping[s].add(e)
    except:
        mapping[s] = set()
        mapping[s].add(e)
        
    try:
        mapping[e].add(s)
    except:
        mapping[e] = set()
        mapping[e].add(s)
    
def check(x, cnt):
    if x == E:
        print(cnt + 1)
        quit()

q = deque()
q.append((S, 0))
while q:
    p, cnt = q.popleft()
    visited[p] = 1

    if p == E:
        print(cnt)
        break
    
    for i in move:
        if 0 < p+i <=N and not visited[p+i]:
            visited[p+i] = 1
            q.append((p+i, cnt+1))
    
    if mapping[p]:
        for i in mapping[p]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, cnt+1))
    