import sys
input = sys.stdin.readline

N, M = map(int ,input().split())
ary = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            ary[i][j] = 0
        else:
            ary[i][j] = sys.maxsize

for _ in range(M):
    A, B, C = map(int, input().split())
    ary[A][B] = C
    ary[B][A] = C
    
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            ary[j][k] = min(ary[j][k], ary[j][i] + ary[i][k])
       
min_size = sys.maxsize    
answ = 0
for i in range(1, N+1):
    ex = 0
    for j in range(1, N+1):
        ex += ary[i][j]
    if ex < min_size:
        min_size = ex
        answ = i
    

print(answ)