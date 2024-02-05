# 5번 받아쓰기

N, M = map(int, input().split())
wrong = list(input().rstrip())
answ = list(input().rstrip())

dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, M+1):
    dp[0][i] = i

for i in range(1, N+1):
    dp[i][0] = i

for i in range(N):
    for j in range(M):
        dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
        
        if answ[j] == wrong[i] or (wrong[i] == 'i' and answ[j] in 'jl') or (wrong[i] == 'v' and answ[j] == 'w'):
            dp[i+1][j+1] = dp[i][j]

print(dp[N][M])