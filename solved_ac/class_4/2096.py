# 내려가기
import sys
input = sys.stdin.readline

N = int(input())
ary = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*2 for _ in range(3)] for _ in range(2)]

for i in range(1, N+1):
    dp[(i-1)%2][0][0] = max(dp[i%2][0][0], dp[i%2][1][0]) + ary[i-1][0]
    dp[(i-1)%2][1][0] = max(dp[i%2][0][0], dp[i%2][1][0], dp[i%2][2][0]) + ary[i-1][1]
    dp[(i-1)%2][2][0] = max(dp[i%2][1][0], dp[i%2][2][0]) + ary[i-1][2]
    
    dp[(i-1)%2][0][1] = min(dp[i%2][0][1], dp[i%2][1][1]) + ary[i-1][0]
    dp[(i-1)%2][1][1] = min(dp[i%2][0][1], dp[i%2][1][1], dp[i%2][2][1]) + ary[i-1][1]
    dp[(i-1)%2][2][1] = min(dp[i%2][1][1], dp[i%2][2][1]) + ary[i-1][2]

print(max(dp[(N-1)%2][0][0], dp[(N-1)%2][1][0], dp[(N-1)%2][2][0]), min(dp[(N-1)%2][0][1], dp[(N-1)%2][1][1], dp[(N-1)%2][2][1]))
