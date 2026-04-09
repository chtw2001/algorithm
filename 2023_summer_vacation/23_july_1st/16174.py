import sys
input = sys.stdin.readline

n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))

visited = [[1]*n for _ in range(n)]

def check(x, y):
    if maze[x][y] == -1:
        print("HaruHaru")
        quit()
        
    if maze[x][y]: # 0이면 시간초과인가?
        ex = maze[x][y]
        if 0 <= x+ex < n and 0 <= y < n and visited[x+ex][y]:
            visited[x+ex][y] = 0
            check(x+ex, y)
            
        if 0 <= x < n and 0 <= y+ex < n and visited[x][y+ex]:
            visited[x][y+ex] = 0
            check(x, y+ex)

check(0, 0)
print("Hing")