import sys
input = sys.stdin.readline

# m => height, n => width
m, n = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(m)]

if maze[0][0] == -1:
    print(-1)
    quit()

move = [[0,-1],[0,1],[1,0],[-1,0]]

# x => height, y => width
def check(x, y, cnt, answ):
    if x == m-1 and y == n-1:
        answ = min(answ, cnt)
        return answ
    if cnt > answ:
        return -1
    for i, j in move:
        if 0 <= x+i < m and 0 <= y+j < n and visited[x+i][y+j] and maze[x+i][y+j]!= -1:
            visited[x+i][y+j] = False
            check(x+i, y+j, cnt+maze[x+i][y+1], answ)
            visited[x+i][y+j] = True

    visited = [[True]*n]*m

# dfs로 해야함 무조건