# 2번
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(R)]
T = int(input())

answ = 0

for i in range(R-2):
    for j in range(C-2):
        ex = []
        for k in range(3):
            for r in range(3):
                ex.append(ary[i+k][j+r])
        ex.sort()
        if ex[4] >= T:
            answ += 1
        del ex

print(answ)
    