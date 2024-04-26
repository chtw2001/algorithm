# 3번 시그널
from collections import deque
N = int(input())
string = input().rstrip()
X, Y = N//5, 5
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(y, x):
    q = deque()
    q.append((y, x))
    visited = set()
    visited.add((y, x))
    volumn = 0
    while q:
        y, x = q.popleft()
        volumn += 1
        for i, j in move:
            dx, dy = x+i, y+j
            if 0 <= dx < X and 0 <= dy < Y:
                if (dy, dx) not in visited and ary[dy][dx]:
                    visited.add((dy, dx))
                    q.append((dy, dx))

    return volumn

ary = [[0]*(X) for _ in range(Y)]
for i in range(Y):
    for j in range(X):
        if string[i*(X) + j] == '#':
            ary[i][j] = 1

start_idx = []
for i in range(X):
    if ary[0][i]:
        start_idx.append((0, i))

answ_ary = []

i = 0
while i < len(start_idx):
    y, x = start_idx[i]
    volumn = dfs(y, x)
    if volumn == 5:
        answ_ary.append(1)
        i -= 2
    elif volumn == 9:
        answ_ary.append(4)
        i -= 1
    elif volumn == 7:
        answ_ary.append(7)
    elif volumn == 13:
        answ_ary.append(8)
    elif volumn == 11:
        if not ary[y+1][x+2]:
            answ_ary.append(5)
        elif not ary[y+3][x+2]:
            answ_ary.append(2)
        else:
            answ_ary.append(3)
    else:
        if not ary[y+3][x]:
            answ_ary.append(9)
        elif not ary[y+1][x+2]:
            answ_ary.append(6)
        else:
            answ_ary.append(0)
    i += 3

for num in answ_ary:
    print(num, end='')