# 3번 강아지는 많을수록 좋다

import sys
from collections import deque
input = sys.stdin.readline

N, M, A, B = map(int, input().split())
area = [0]*(N+1)
while M:
    s, e = map(int, input().split())
    for i in range(s, e+1):
        area[i] = 1
    
    M -= 1
    
q = deque()
q.append((0, 0))
visited = [0]*(N+1)
while q:
    dog_num, cnt = q.popleft()
    if dog_num == N:
        print(cnt)
        quit()
    for sum in [A, B]:
        if dog_num+sum <= N:
            if not area[dog_num+sum] and not visited[dog_num+sum]:
                visited[dog_num+sum] = 1
                q.append((dog_num+sum, cnt+1))

print(-1)