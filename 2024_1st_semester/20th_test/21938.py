# 3번 영상처리
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(N)]
T = int(input())

def bfs(row, col):
    q = deque()
    q.append((row, col))
    ary[row][col] = 0
    while q:
        x, y = q.popleft()
        for i, j in move:
            dx, dy = x+i, y+j
            if 0 <= dx < N and 0 <= dy < M:
                if not ary[dx][dy]:
                    continue
                q.append((dx, dy))
                ary[dx][dy] = 0


ary = [[] for _ in range(N)]
for i in range(N):
    for j in range(0, M*3, 3):
        if (list_[i][j] + list_[i][j+1] + list_[i][j+2])//3 >= T:
            ary[i].append(1)
        else:
            ary[i].append(0)


move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
answ = 0
for i in range(N):
    for j in range(M):
        if not ary[i][j]:
            continue

        bfs(i, j)
        answ += 1

print(answ)
