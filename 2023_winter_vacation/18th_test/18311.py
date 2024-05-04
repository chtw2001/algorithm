# 1번 왕복
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ary = list(map(int, input().split()))
cal_ary = [[[0], [0, 0], [0, 0]] for _ in range(N)]

s = 0
for i in range(N):
    area = i
    start = s
    if i == N-1:
        end = s + ary[i]
    else:
        end = s + ary[i] - 1
    cal_ary[i][0] = area
    cal_ary[i][1][0] = start
    cal_ary[i][1][1] = end
    s = end + 1

s -= 1
for i in range(N-1, -1, -1):
    area = i
    start = s
    if i == 0:
        end = s + ary[i]
    else:
        end = s + ary[i] - 1
    cal_ary[i][2][0] = start
    cal_ary[i][2][1] = end
    s = end + 1

for i in range(N):
    if cal_ary[i][1][0] <= K <= cal_ary[i][1][1]:
        print(cal_ary[i][0]+1)
        quit()
    elif cal_ary[i][2][0] <= K <= cal_ary[i][2][1]:
        print(cal_ary[i][0]+1)
        quit()
    