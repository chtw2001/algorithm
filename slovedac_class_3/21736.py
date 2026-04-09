import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(str, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

I, answ = 0, 0
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'I':
            I = (i, j)


q = deque()
q.append((I[0], I[1]))
while q:
    x, y = q.popleft()
    visited[x][y] = 1
    if maze[x][y] == 'P':
        answ += 1
    for i, j in move:
        dx, dy = x+i, y+j
        if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy] and maze[dx][dy] != 'X':
            q.append((dx, dy))
            visited[dx][dy] = 1

if not answ:
    print('TT')
else:
    print(answ)

