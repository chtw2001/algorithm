# 가장 긴 감소하는 부분 수열
# dp 풀이 O(N^2)
# https://www.youtube.com/watch?v=fV-TF4OvZpk
N = int(input())
ary = list(map(int, input().split()))

dp = [1]*(N+1)

for i in range(N):
    for j in range(i):
        if ary[i] < ary[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))