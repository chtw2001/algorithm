# 4번 박물관 견학

import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline
N, M = map(int, input().split())
ary = []

for _ in range(N):
    ex = list(map(int, input().split()))
    start, end = ex[1]-1, ex[-1]-1
    ary.append([start, end])

min_heap, max_heap = [], []
for i in range(N):
    push(max_heap, -ary[i][0])
    push(min_heap, ary[i][1])
    while -max_heap[0] > min_heap[0]:
        push(max_heap, -pop(min_heap))
        push(min_heap, -pop(max_heap))

print(abs(pop(max_heap))+1)