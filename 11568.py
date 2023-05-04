import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1201)
n = int(input())
maze = list(map(int, input().split()))
# dp = [[0]*1001 for _ in range(1001)]
dp = [0]*1001
maze.insert(0,0)

for i in range(1, n+1):
    ex = 0
    for j in range(i):
        if maze[j] < maze[i]:
            ex = max(ex, dp[j])
        dp[i] = ex + 1

print(max(dp))



# def check(pre, k):
#     if k == n+1:
#         return 0
#     if dp[pre][k] != 0:
#         return dp[pre][k]
#     if maze[pre] < maze[k]:
#         dp[pre][k] = max(check(pre, k+1), check(k, k+1)+1)
#     else:
#         dp[pre][k] = check(pre, k+1)

#     return dp[pre][k]

# print(check(0, 1))

# 재귀 92% 시간초과