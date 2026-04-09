import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

maze = [[sys.maxsize]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    maze[s][e] = min(maze[s][e], cost)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if k != i and k != j and i != j:
                maze[i][j] = min(maze[i][j], maze[i][k] + maze[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if maze[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(maze[i][j], end=' ')
    print()
