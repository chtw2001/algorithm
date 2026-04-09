# 특정 거리의 도시 찾기
import sys
from collections import defaultdict
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
path_info = defaultdict(list)

for _ in range(M):
    s, e = map(int, input().split())
    path_info[s].append((1, e)) # path[start] = cost, destination


def Dijkstra(start):
    path = [sys.maxsize]*(N+1)
    path[start] = 0
    q = []
    push(q, (0, start))
    while q:
        cost, destination = pop(q)
        
        if path[destination] < cost:
            continue
        
        for new_cost, new_destination in path_info[destination]:
            if path[new_destination] > cost + new_cost:
                path[new_destination] = cost + new_cost
                push(q, (path[new_destination], new_destination))
    
    return path


result = Dijkstra(X)
answ = []
for idx, cost in enumerate(result[1:]):
    if cost == K:
        answ.append(idx+1)

if answ:
    for city in sorted(answ):
        print(city)
else:
    print(-1)
