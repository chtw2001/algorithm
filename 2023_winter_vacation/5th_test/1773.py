# 1번 폭죽쇼

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
ary = [int(input()) for _ in range(N)]

answ = [0]*(C+1)

for ele in ary:
    ex = ele
    while ex < C+1:
       answ[ex] = 1
       ex += ele

cnt = 0
for i in range(C+1):
    if answ[i]:
        cnt += 1

print(cnt)