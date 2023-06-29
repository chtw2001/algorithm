import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

n, m = map(int, input().split())
belif = [set() for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    belif[b].add(a)

def check(n, cnt, m):
    if not belif[n]:
        return cnt
    if answ[n]:
        return answ[n]+cnt
    for i in belif[n]:
        m = max(m, check(i, cnt+1, m))
    answ[n] = m
    return m

answ = [0 for _ in range(n+1)]
for i in range(1, n+1):
    check(i, 0, 0)
    print(i, answ)
print(answ)

answ2 = []
ex = 0
for i in range(1, n+1):
    if answ[i] >= ex:
        push(answ2, (-answ[i], i))
    ex = answ[i]

while True:
    ex = pop(answ2)
    print(ex[1], end=' ')
    if ex[0] != answ2[0][0]:
        break