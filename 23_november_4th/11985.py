import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
ary = [int(input()) for _ in range(N)]
ary.insert(0, 0)
dp = [0]*(N+1)

dp[1] = K

for i in range(2, N+1):
    MAX, MIN = ary[i], ary[i]
    dp[i] = dp[i-1] + K # only one orange

    for orange_num in range(2, M+1):
        left_idx = i - orange_num + 1
        if left_idx < 1:
            break

        MAX, MIN = max(MAX, ary[left_idx]), min(MIN, ary[left_idx])
        cost = K + orange_num*(MAX - MIN)
        dp[i] = min(dp[i], dp[left_idx-1] + cost)

print(dp[N])

#ref: https://limdongjin.github.io/problemsolving/boj_11985.html