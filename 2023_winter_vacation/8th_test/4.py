# 4번
N = int(input())
string = list(input().rstrip())
dp = [0]*(N+1)
order = [0]*(N+1)

for i in range(N):
    if string[i] == 'W':
        order[i] = 1
    elif string[i] == 'H':
        order[i] = 2
    elif string[i] == 'E':
        order[i] = 3


for i in range(N):
    for j in range(i):
        if order[i] and order[i] >= order[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))