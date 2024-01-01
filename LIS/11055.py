# 가장 큰 증가하는 부분 수열
# 0번째 인덱스가 가장 커도 그 또한 부분수열이라서 괜찮음
N = int(input())
ary = list(map(int, input().split()))
dp = [1]*(N+1)
dp[0] = ary[0]

for i in range(N):
    for j in range(i):
        if ary[i] > ary[j]:
            dp[i] = max(dp[i], dp[j] + ary[i])
        else:
            dp[i] = max(dp[i], ary[i])

print(max(dp))
