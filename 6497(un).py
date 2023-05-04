import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    maze = []
    for _ in range(m):
        maze.append(list(map(int, input().split())))
    
    