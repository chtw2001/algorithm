import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(M)]
ary.insert(0,0)

dp = [[0]*(N+1) for _ in range(M+1)]
for i in range(1, M+1):     # i => 물건의 인덱스, ary[i][0] => 물건의 크기, ary[i][1] => 물건의 가치
    for j in range(1, N+1): # 배낭의 크기
        if ary[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-ary[i][0]] + ary[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[M][N])
