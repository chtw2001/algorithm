# 최단경로
import sys
from heapq import heappush as push, heappop as pop
from collections import defaultdict

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
path = [2000001]*(V+1)
path[K] = 0
# edge = defaultdict(list)
edge = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edge[u].append((w, v))

q = []
push(q, (0, K))

while q:
    weight, vertex = pop(q)
    if path[vertex] < weight:
        continue
    
    for w, v in edge[vertex]:
        if weight + w < path[v]:
            path[v] = weight + w
            push(q, (weight + w, v))

for i in range(1, V+1):
    if path[i] == 2000001:
        print("INF")
    else:
        print(path[i])