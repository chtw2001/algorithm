import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

answ = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and maze[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            while q:
                a, b = map(int, q.popleft())
                for x, y in move:
                    if 0 <= x + a < N and 0 <= y + b < M and not visited[a+x][b+y] and maze[a+x][b+y]:
                        q.append((a+x, b+y))
                        visited[a+x][b+y] = 1
            answ += 1

print(answ)