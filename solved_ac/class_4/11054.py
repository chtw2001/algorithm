# 가장 긴 바이토닉 부분 수열
import sys
N = int(input())
ary = list(map(int, input().split()))

dp = [1]*(N+1)
for i in range(1, N):
    for j in range(i):
        if ary[i] > ary[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(1, N):
    for j in range(i):
        if ary[i] < ary[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
