from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = []
start = [] # 위쪽에서 아래로 전류가 흐르는데, 맨 위에부터 시작점이기 때문에 설정
move = [[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(n):
    if _ == 0:
        ex = list(map(int, input().strip()))
        for i in range(len(ex)):
            if ex[i] == 0:
                start.append([0, i])
        maze.append(ex)
    else:
        maze.append(list(map(int, input().strip())))

q = deque()
visited = [[1]*m for _ in range(n)] # 이미 방문한 칸은 계속 유지
for i in range(len(start)): # 시작점으로 잡은 친구들을 한개씩 뽑음
    q.append(start[i])
    while q:
        x, y = q.popleft()
        visited[x][y] = 0
        for i, j in move:
            if 0 <= x+i < n and 0 <= y+j < m and visited[x+i][y+j] and not maze[x+i][y+j]:
                if x+i == n-1:
                    print('YES')
                    quit()
                q.append([x+i, y+j])
                visited[x+i][y+j] = 0

print('NO')