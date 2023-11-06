import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(M)]
maze2 = [[0]*N for _ in range(M)]

for i in range(M-1, -1, -1):
    cnt = 1
    for j in range(N-1, -1, -1):
        if maze[i][j] == 0:
            maze2[i][j] = cnt
            cnt += 1
        else:
            cnt = 1

for i in range(N):
    for j in range(M):
        