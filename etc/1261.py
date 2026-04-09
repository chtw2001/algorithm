from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(N)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dijkstra():
    path = [[sys.maxsize]*M for _ in range(N)]
    path[0][0] = 0
    q = []
    push(q, (0, (0,0)))
    
    while q:
        cost, pos = pop(q)
        if path[pos[0]][pos[1]] < cost:
            continue
        
        for i, j in move:
            dx, dy = pos[0]+i, pos[1]+j
            if dx < 0 or dy < 0 or dx >= N or dy >= M:
                continue
            
            if path[dx][dy] > cost + int(maze[dx][dy]):
                path[dx][dy] = cost + int(maze[dx][dy])
                push(q, (path[dx][dy], (dx, dy)))

    return path[-1][-1]

print(dijkstra())
