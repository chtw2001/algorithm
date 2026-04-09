import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

N = int(input())
q = []
answ = 0
for i in range(N):
    ex = list(map(int, input().split()))
    if not ex[0]:
        if not q:
            continue
        
        q[0][2] -= 1
        if not q[0][2]:
            t, n, d = pop(q)
            answ += n
            
        continue
    push(q, [-i, ex[1], ex[2]-1])
    if not q[0][2]:
        t, n, d = pop(q)
        answ += n

print(answ)