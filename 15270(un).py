import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [[] for _ in range(n+1)]
ch = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    maze[a].append(b)
    maze[b].append(a)

