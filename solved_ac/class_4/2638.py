import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [[0]*M for _ in range(N)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]# , (1, 1), (1, -1), (-1, 1), (-1, -1)]
cheeze = set()
for i in range(N):
    ex = list(map(int, input().split()))
    for j in range(M):
        if ex[j]:
            maze[i][j] = 1
            cheeze.add((i, j))

def check_outside(pos:tuple, outside:set):
    q = deque()
    q.append(pos)
    outside.add(pos)
    
    while q:
        x, y = q.popleft()
        for i, j in move:
            dx, dy = x+i, y+j
            if 0 <= dx < N and 0 <= dy < M:
                if (dx, dy) not in outside:
                    if not maze[dx][dy]:
                        outside.add((dx, dy))
                        q.append((dx, dy))
    return outside

def check_melting(cheeze:set, outside:set):
    melting_cheeze = set()
    for i, j in cheeze:
        ex = 0
        for x, y in move:
            dx, dy = i+x, j+y
            if not maze[dx][dy] and (dx, dy) in outside:
                ex += 1
        if ex >= 2:
            melting_cheeze.add((i, j))
            maze[i][j] = 0
            
    for i, j in melting_cheeze:
        cheeze.discard((i, j))
        outside.add((i, j))
        outside = check_outside((i, j), outside)
            
    return (cheeze, outside)

answ = 0
outside = set()
for i in range(N):
    for j in range(M):
        if (i, j) in outside:
            continue
        if not maze[i][j]:
            outside = check_outside((i, j), outside)
        cheeze, outside = check_melting(cheeze, outside)
        answ += 1

print(answ)