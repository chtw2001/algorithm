import sys
from collections import deque
input = sys.stdin.readline

X, Y ,N = map(int, input().split())
ary = [[0]*(1001) for _ in range(1001)]
visited = [[0]*(1001) for _ in range(1001)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(N):
    x, y = map(int, input().split())
    ary[x+500][y+500] = 1 # 웅덩이
    
q = deque()
q.append((500, 500, 0))
visited[500][500] = 1
while q:
    x, y, cost = q.popleft()
    if x == X+500 and y == Y+500:
        print(cost)
        quit()
    for i, j in move:
        dx, dy = x+i, y+j
        if (0 <= dx <= 1000 and 0 <= dy <= 1000):
            if not ary[dx][dy]:
                if not visited[dx][dy]:
                    visited[dx][dy] = 1
                    q.append((dx, dy, cost+1))
