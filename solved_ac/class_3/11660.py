# 구간 합 구하기 5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
psum_table = table.copy()

for i in range(N):
    for j in range(1, N):
        psum_table[i][j] += psum_table[i][j-1]

for i in range(N):
    psum_table[i].insert(0,0)


while M:
    x1, y1, x2, y2 = map(int, input().split())
    r = x2 - x1
    answ = 0
    for i in range(x1-1, x2):
        answ += psum_table[i][y2] - psum_table[i][y1-1]
    
    print(answ)
    M -= 1