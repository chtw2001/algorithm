from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]

q = deque()
visited = set()

q.append((0, 0))
visited.add((0, 0))

while q:
    x, y = map(int, q.popleft())
    if maze[x][y] == -1:
        print('HaruHaru')
        quit()
    
    move = maze[x][y]
    if 0 <= x + move < N and 0 <= y < N:
        if (x+move, y) not in visited:
            q.append((x+move, y))
            visited.add((x+move, y))
    
    if 0 <= x < N and 0 <= y + move < N:
        if (x, y+move) not in visited:
            q.append((x, y+move))
            visited.add((x, y+move))

print('Hing')