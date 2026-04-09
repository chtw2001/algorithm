# 4번 게임
from collections import deque
import sys
input = sys.stdin.readline
ary = [[0]*501 for _ in range(501)]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
warn_list = []
for _ in range(N):
    warn_list.append(list(map(int, input().split())))
for x1, y1, x2, y2 in warn_list:
    for i in range(min(x1, x2), max(x1, x2)+1):    # warn
        for j in range(min(y1, y2), max(y1, y2)+1):
            ary[i][j] = 1

M = int(input())
danger_list = []
for _ in range(M):
    danger_list.append(list(map(int, input().split())))
for x1, y1, x2, y2 in danger_list:
    for i in range(min(x1, x2), max(x1, x2)+1):    # danger
        for j in range(min(y1, y2), max(y1, y2)+1):
            ary[i][j] = 2


q = deque()
q.append((0, 0, 0))
ary[0][0] = 2 
while q:
    x, y, life = q.popleft()
    if x == 500 and y == 500:
        print(life)
        quit()
    for i, j in move:
        dx, dy = x+i, y+j
        if 0 <= dx < 501 and 0 <= dy < 501:
            if ary[dx][dy] == 0:
                q.appendleft((dx, dy, life+ary[dx][dy]))
            elif ary[dx][dy] == 1:
                q.append((dx, dy, life+ary[dx][dy]))
            ary[dx][dy] = 2

print(-1)
