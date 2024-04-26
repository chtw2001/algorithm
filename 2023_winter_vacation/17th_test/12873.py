# 2번 기념품
from collections import deque
q = deque()
N = int(input())
for i in range(1, N+1):
    q.append(i)
    
length = N
for i in range(1, N):
    rotate_num = pow(i, 3) % length
    for _ in range(rotate_num):
        q.rotate(-1)
    q.pop()
    length -= 1

print(q.pop())