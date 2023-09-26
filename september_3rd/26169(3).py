import sys
input = sys.stdin.readline

def dfs(r, c, apple, depth):
    if depth < 3:
        for x, y in move:
            if 0 <= r + x <= 4 and 0 <= c + y <= 4 and maze[r+x][c+y] != -1:
                ex = maze[r+x][c+y]
                maze[r+x][c+y] = -1
                dfs(r+x, c+y, apple+ex, depth+1)
                maze[r+x][c+y] = ex

    else:
        if apple >= 2:
            print(1)
            quit()
        else:
            return


maze = [list(map(int, input().split())) for _ in range(5)]
R, C = map(int, input().split())
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
maze[R][C] = -1
dfs(R, C, 0, 0)

print(0)
