# 서강그라운드
import sys
input = sys.stdin.readline

N, M, WAY = map(int, input().split())
groundItemNum = [0]*(N+1)
ground = list(map(int, input().split()))
for i in range(N):
    groundItemNum[i+1] = ground[i] # n번에 m개의 아이템

dp = [[sys.maxsize]*(N+1) for _ in range(N+1)]
for i in range(WAY):
    s, e, cost = map(int, input().split())
    dp[s][e] = cost
    dp[e][s] = cost

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if k != i and k != j and i != j:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

answ = -1
for i in range(1, N+1):
    ex = groundItemNum[i]
    for j in range(1, N+1):
        if i == j:
            continue
        if dp[i][j] <= M:
            ex += groundItemNum[j]
    answ = max(answ, ex)

print(answ)