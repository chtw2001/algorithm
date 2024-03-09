import sys
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))
ary.insert(0, 0)
ary.append(0)
ary.append(0)
dp = [0]*(N+3)
for i in range(1, N+3):
    if i < 3:
        dp[i] = dp[i-1] + ary[i]
        continue
        
    dp[i] = max(dp[i-1] + ary[i], dp[i-3] + 2*(ary[i-2] + ary[i-1] + ary[i]))
print(dp[N+2])
