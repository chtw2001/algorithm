import sys
input = sys.stdin.readline

N, M = map(int, input().split())
paper = set(map(int, input().split()))
not_paper = []
for i in range(1, N+1):
    if i not in paper:
        not_paper.append(i)

dp = [6000]*(N+1)
dp[0] = 0
if 1 in paper:
    dp[1] = 0
else:
    dp[1] = 7

for i in range(2, N+1):
    if i in paper:
        dp[i] = dp[i-1]
        continue

    for p in not_paper:
        if p > i:
            break
        # print(dp[i-1]+7, dp[p-1]+5+2*(i-p+1))
        dp[i] = min(dp[i], dp[i-1]+7, dp[p-1]+5+2*(i-p+1))

print(dp[N])
