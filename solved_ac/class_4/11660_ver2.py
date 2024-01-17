# 구간 합 구하기 5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(1, N):
        table[i][j] += table[i][j-1]

while M:
    x1, y1, x2, y2 = map(int, input().split())
    answ = 0
    
    for i in range(x1-1, x2):
        if y1-2 < 0:
            answ += table[i][y2-1]
        else:
            answ += table[i][y2-1] - table[i][y1-2]
    
    print(answ)
    M -= 1
