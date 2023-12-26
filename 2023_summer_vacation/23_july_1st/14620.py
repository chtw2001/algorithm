from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
ary = [list(map(int, input().split())) for _ in range(n)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cant_go = [(0, 2), (0, -2), (2, 0), (-2, 0),
           (1,1),(1,-1),(-1,1),(-1,-1),
           (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]

cost = defaultdict(int)
for i in range(1, n-1):
    for j in range(1, n-1):
        ex = ary[i][j]
        for x, y in move:
            ex += ary[i+x][j+y]
        cost[(i, j)] = ex

answ = sys.maxsize

def cant_go_f(u, v, d):
    global answ
    if d == 2:
        answ = min(answ, v)
        return
    for i in range(1, n-1):
        for j in range(1, n-1):
            if (i, j) not in u:
                ex = set()
                for nx, ny in cant_go:
                    if (i+nx, j+ny) not in u:
                        ex.add((i+nx, j+ny))
                    u.add((i+nx, j+ny))
                cant_go_f(u, v+cost[(i, j)], d+1)
                for nx, ny in ex:
                    u.discard((nx, ny))
    

for i in range(1, n-1):
    for j in range(1, n-1):
        ex = set()
        for nx, ny in cant_go:
            ex.add((i+nx, j+ny))
        cant_go_f(ex, cost[(i, j)], 0)

print(answ)