import sys
input = sys.stdin.readline

N, M = map(int, input().split())
package = [list(map(int, input().split())) for _ in range(N)] # [무게, 가치]
package.insert(0, 0)
dp = [[0]*(M+1) for _ in range(N+1)]

for item in range(1, N+1):
    for weight in range(1, M+1):
        if package[item][0] > weight:
            dp[item][weight] = dp[item-1][weight]
        else:
            dp[item][weight] = max(dp[item-1][weight], dp[item-1][weight-package[item][0]] + package[item][1])
            
print(dp[N][M])
