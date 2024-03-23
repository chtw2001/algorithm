import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    path = [sys.maxsize]*(N+1)
    path[start] = 0
    q = []
    push(q, (0, start))
    while q:
        w, p = pop(q)
        if path[p] < w:
            continue
        
        for w_, p_ in graph[p]:
            if w + w_ < path[p_]:
                path[p_] = w + w_
                push(q, (w_ + w, p_))
    
    return path[end]

one_to_v1 = dijkstra(1, v1)
one_to_v2 = dijkstra(1, v2)
v1_to_v2 = dijkstra(v1, v2)
v2_to_v1 = dijkstra(v2, v1)
v1_to_n = dijkstra(v1, N)
v2_to_n = dijkstra(v2, N)

answ = sys.maxsize
if one_to_v1 != sys.maxsize:
    if v1_to_v2 != sys.maxsize:
        if v2_to_n != sys.maxsize:
            answ = one_to_v1 + v1_to_v2 + v2_to_n

if one_to_v2 != sys.maxsize:
    if v2_to_v1 != sys.maxsize:
        if v2_to_n != sys.maxsize:
            answ = min(answ, one_to_v2 + v2_to_v1 + v1_to_n)

if answ == sys.maxsize:
    print(-1)
else:
    print(answ)
