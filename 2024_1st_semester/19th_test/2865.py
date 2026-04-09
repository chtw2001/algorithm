# 1번 나는 위대한 슈퍼스타K
import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline
N, M, K = map(int, input().split())
people = set()
answ_heap = []

for _ in range(M):
    ex = list(map(float, input().split()))
    for i in range(0, N*2, 2):
        push(answ_heap, (-ex[i+1], ex[i]))

answ = 0
i = 0
while i < K:
    ex = pop(answ_heap)
    if ex[1] in people:
        continue
    answ -= ex[0]
    people.add(ex[1])
    i += 1

print(round(answ, 1))
