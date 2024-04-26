# 3번

import sys
N, a, b = map(int,input().split())
dp = [sys.maxsize]*(N+1)
dp[0] = 0
for i in range(N+1):
    if i+1 <= N:
        dp[i+1] = min(dp[i+1], dp[i] + 1)
    if i+a+1 <= N:
        dp[i+a+1] = min(dp[i+a+1], dp[i] + 1)
    if i+b+1 <= N:
        dp[i+b+1] = min(dp[i+b+1], dp[i] + 1)
        
print(dp[N])
