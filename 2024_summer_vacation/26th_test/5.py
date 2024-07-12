import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

N, H, T = map(int, input().split())
q = []
for _ in range(N):
    push(q, -int(input()))

for i in range(T):
    if H > -q[0]:
        print('YES')
        print(i)
        quit()
        
    ex = -pop(q)
    if ex == 1:
        push(q, -ex)
    else:
        push(q, -(ex // 2))

if H > -q[0]:
    print('YES')
    print(T)
    quit()

print('NO')
print(-q[0])
