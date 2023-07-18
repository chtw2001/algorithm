from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
move = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]


def same_num(x, y):
    same = [(x, y)]
    q = deque()
    q.append((x, y))
    visited = [[1]*M for _ in range(N)]
    visited[x][y] = 0
    num = maze[x][y]
    while q:
        ex = q.popleft()
        for d in move:
            if 0 <= ex[0]+d[0] < N and 0 <= ex[1]+d[1] < M and visited[ex[0]+d[0]][ex[1]+d[1]]:
                if num == maze[ex[0]+d[0]][ex[1]+d[1]]:
                    q.append((ex[0]+d[0], ex[1]+d[1]))
                    same.append((ex[0]+d[0], ex[1]+d[1]))
                    visited[ex[0]+d[0]][ex[1]+d[1]] = 0
    return (same, num)

def around_num(q, num, v):
    visited = set()
    made = 1
    for i in q:
        visited.add(i)
    for ex in q:
        for d in move:
            if 0 <= ex[0]+d[0] < N and 0 <= ex[1]+d[1] < M and (ex[0]+d[0], ex[1]+d[1]) not in visited:
                if num < maze[ex[0]+d[0]][ex[1]+d[1]]:
                    break
                else:
                    visited.add((ex[0]+d[0], ex[1]+d[1]))
                    
        if 0 <= ex[0]+d[0] < N and 0 <= ex[1]+d[1] < M and num < maze[ex[0]+d[0]][ex[1]+d[1]]:
            made = 0
            break
    for ex in q:
        v[ex[0]][ex[1]] = 0

    if made:
        for ex in q:
            maze[ex[0]][ex[1]] = 501
        return 1
    return 0

answ = 0
v = [[1]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if maze[i][j] != 501 and v[i][j]:
            s, n = same_num(i, j)
            answ += around_num(s, n, v)
            
print(answ)