import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
ary = [list(input().rstrip()) for _ in range(N)]
move = [[0, 1], [1, 0], [-1, 0], [0, -1]]
food = dict()
pos = 0
for i in range(N):
    for j in range(M):
        if ary[i][j] == '2':
            pos = [int(i), int(j)]
        elif ary[i][j] in ['3', '4', '5']:
            food[(i, j)] = 1

q = deque()
q.append([pos[0], pos[1], 0])
visited = [[0]*M for _ in range(N)]
visited[pos[0]][pos[1]] = 1
while q:
    x, y, cnt = q.popleft()
    for i, j in move:
        dx, dy = x + i, y + j
        if dx < 0 or dx >= N or dy < 0 or dy >= M or visited[dx][dy] or ary[dx][dy] == '1':
            continue
        try:
            if food[(dx, dy)]:
                print("TAK")
                print(cnt+1)
                quit()
        except KeyError:
            pass
        visited[dx][dy] = 1
        q.append([dx, dy, cnt+1])
    
        
print("NIE")
