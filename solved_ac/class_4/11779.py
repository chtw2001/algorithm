# 최소비용 구하기 2
from heapq import heappush as push, heappop as pop
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
ary = defaultdict(list)
for _ in range(M):
    s, e, c = map(int, input().split())
    ary[s].append((e, c))

S, E = map(int, input().split())
distance = [[sys.maxsize, []] for _ in range(N+1)]
distance[S][0] = 0
distance[S][1].append(S)

q = []
push(q, (0, S))
while q:
    cur_distance, s = pop(q)
    
    if distance[s][0] < cur_distance:
        continue
    
    for new_s, new_distance in ary[s]:
        d = cur_distance + new_distance
        if d < distance[new_s][0]:
            distance[new_s][0] = d
            distance[new_s][1] = distance[s][1].copy()
            distance[new_s][1].append(new_s)
            push(q, (d, new_s))

print(distance[E][0])
print(len(distance[E][1]))
print(*distance[E][1])
