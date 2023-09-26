from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    val = 0
    maze[x][y] = 1

    while q:
        element = q.popleft()
        val += 1
        x, y = element[0], element[1]
        for _x, _y in move:
            if 0 <= x + _x < N and 0 <= y + _y < N and not maze[x+_x][y+_y]:
                q.append((x+_x, y+_y))
                maze[x+_x][y+_y] = 1
            
    return val


N, M, K = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
room = []

for i in range(N):
    for j in range(N):
        if maze[i][j]:
            continue
        res = bfs(i, j)
        if res:
            room.append(res)

need = 0 # number of mushroom master needed

for num in room:
    if num % K:
        need += num // K + 1
    else:
        need += num // K
        
if not need:
    print('IMPOSSIBLE')
elif M < need:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
    print(M - need)
