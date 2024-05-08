# 웜홀
import sys
input = sys.stdin.readline

TC = int(input())
while TC:
    N, M, W = map(int, input().split())
    ary = [[10001]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        ary[S][E] = min(ary[S][E], T)
        ary[E][S] = min(ary[E][S], T)
    for _ in range(W):
        S, E, T = map(int, input().split())
        ary[S][E] = min(ary[S][E], -T)
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if k == i or k == j or i == j:
                    continue
                ary[i][j] = min(ary[i][j], ary[i][k] + ary[k][j])

    answ = "NO"
    for i in range(1, N+1):
        for j in range(1, N+1):
            if ary[i][j] < 0 and ary[i][j] + ary[j][i] < 0:
                answ = "YES"

    print(answ)
    
    TC -= 1
