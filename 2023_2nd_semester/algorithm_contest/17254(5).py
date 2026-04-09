from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

q = []
n, m = map(int, input().split())
for _ in range(m):
    a, b, c = map(str, input().split())
    push(q, [int(b), int(a), c])

while q:
    ex = pop(q)
    print(ex[-1], end='')