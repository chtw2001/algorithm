from collections import deque
from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
move = [[0,1],[0,-1],[1,0],[-1,0]]
maze = []

for _ in range(n):
    ex = list(input().strip())
    for i in range(m):
        if ex[i] == 'F':
            flower = [_, i] 
        elif ex[i] == 'S':
            start = [_, i]
    maze.append(ex)

def check(G, g, x, y):
    for i, j in move:
        if 0 <= x+i < n and 0 <= y+j < m and maze[x+i][y+j] == 'g':
            return [G, g+1, x, y]
    return [G, g, x, y]

q = []
push(q, [0, 0, start[0], start[1]])
answ = [-1,-1,-1,-1]
visited = [[1]*m for _ in range(n)]
while q:
    ex = pop(q)
    if ex == answ:
        print(answ[0], answ[1])
        quit()
    visited[ex[2]][ex[3]] = 0
    for i, j in move:
        if 0 <= ex[2]+i < n and 0 <= ex[3]+j < m and visited[ex[2]+i][ex[3]+j]:
            if maze[ex[2]+i][ex[3]+j] == 'g':
                visited[ex[2]+i][ex[3]+j] = 0
                push(q, [ex[0]+1, ex[1], ex[2]+i, ex[3]+j])
            elif maze[ex[2]+i][ex[3]+j] == '.':
                visited[ex[2]+i][ex[3]+j] = 0
                push(q, check(ex[0], ex[1], ex[2]+i, ex[3]+j))
            elif maze[ex[2]+i][ex[3]+j] == 'F':
                push(q, [ex[0], ex[1], ex[2]+i, ex[3]+j])
                answ = q[0]