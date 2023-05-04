from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
virus = []
allowed = []
maze = []
move = [[0,1],[0,-1],[1,0],[-1,0]]

for i in range(n):
    ex = list(map(int, input().split()))
    for j in range(m):
        if ex[j] == 2:
            virus.append([i,j])
        elif ex[j] == 0:
            allowed.append([i,j])
    maze.append(ex)
a = [arr[:] for arr in maze]

def virus_move(map, x, y):
    ex = [arr[:] for arr in map]
    q = deque()
    q.append([x, y])
    while q:
        loc = q.popleft()
        for i, j in move:
            if 0 <= loc[0] + i < n and 0 <= loc[1] + j < m and ex[loc[0]+i][loc[1]+j] == 0:
                q.append([loc[0]+i, loc[1]+j])
                ex[loc[0]+i][loc[1]+j] = 2
    return ex

def check(map):
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                return [i, j]
    return 0

def zero_move(map):
    ex = [arr[:] for arr in map]
    cnt = [0]
    while True:
        location = check(ex)
        if location:
            ex = zero_area(ex, location[0], location[1])
            cnt.append(ex[0])
            ex = ex[1]
        else:
            return sum(cnt)

def zero_area(map, x, y):
    ex = [arr[:] for arr in map]
    q = deque()
    q.append([x, y])
    ex[x][y] = 1
    cnt = 1
    while q:
        loc = q.popleft()
        for i, j in move:
            if 0 <= loc[0] + i < n and 0 <= loc[1] + j < m and ex[loc[0]+i][loc[1]+j] == 0:
                q.append([loc[0]+i, loc[1]+j])
                cnt += 1
                ex[loc[0]+i][loc[1]+j] = 1
    return [cnt, ex]

answ = []
for i in range(len(allowed)-2):
    for j in range(i+1, len(allowed)-1):
        for k in range(j+1, len(allowed)):
            ex = [arr[:] for arr in maze]
            ex[allowed[i][0]][allowed[i][1]] = 1
            ex[allowed[j][0]][allowed[j][1]] = 1
            ex[allowed[k][0]][allowed[k][1]] = 1
            for q, w in virus:
                ex = virus_move(ex, q, w)
            answ.append(zero_move(ex))

print(max(answ))