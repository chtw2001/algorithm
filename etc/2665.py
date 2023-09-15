from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

n = int(input())
maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[2500]*n for _ in range(n)]

q = []
push(q, (0, 0, 0))

move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

while True:
    cnt, x, y = pop(q)
    if x == n-1 and y == n-1:
        print(cnt)
        quit()
    for i, j in move:
        if 0 <= x+i < n and 0 <= y+j < n:
                if maze[x+i][y+j] and visited[x+i][y+j] > cnt:
                    push(q, (cnt, x+i, y+j))
                    visited[x+i][y+j] = cnt
                elif visited[x+i][y+j] > cnt+1:
                    push(q, (cnt+1, x+i, y+j))
                    visited[x+i][y+j] = cnt + 1