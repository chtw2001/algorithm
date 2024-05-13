# 3번 콘센트
from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ary = sorted(list(map(int, input().split())))

q = [0]*M
for i in ary:
    ex = pop(q)
    push(q, ex+i)

answ_1 = 0
while q:
    answ_1 = max(answ_1, pop(q))

q = [0]*M
for i in ary[::-1]:
    ex = pop(q)
    push(q, ex+i)

answ_2 = 0
while q:
    answ_2 = max(answ_2, pop(q))

print(min(answ_1, answ_2))
