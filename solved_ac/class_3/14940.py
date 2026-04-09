import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answ = [[0]*M for _ in range(N)]
move = [(1, 0), [-1, 0], [0, 1], [0, -1]]
target = []

flag = 0
for i in range(N):
    for j in range(M):
        if maze[i][j] == 2:
            target = [i, j]
            flag = 1
            break
    if flag:
        break

q = deque()
q.append((target[0], target[1], 0))
maze[target[0]][target[1]] = 0
visited[target[0]][target[1]] = True
while q:
    x, y, v = map(int, q.popleft())
    answ[x][y] = v
    for i, j in move:
        if 0 <= x+i < N and 0 <= y+j < M and maze[x+i][y+j] and not visited[x+i][y+j]:
            q.append((x+i, y+j, v+1))
            maze[x+i][y+j] = 0
            visited[x+i][y+j] = True

for i in range(N):
    for j in range(M):
        if maze[i][j]:
            answ[i][j] = -1

for rows in answ:
    print(' '.join(map(str, rows)))
