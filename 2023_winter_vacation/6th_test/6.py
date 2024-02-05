# 6번

import sys
input = sys.stdin.readline
N = int(input())
star, trash = [], []
row, column = [0]*N, [0]*N # 1 => can't go 
for i in range(N):
    ex = input().rstrip()
    for j in range(N):
        if ex[j] == 2:
            row[i], column[j] = 1, 1
            star.append((i, j))
        else:
            row[i], column[j] = 1, 1
            trash.append((i, j))

