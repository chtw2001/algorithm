# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# maze = [list(map(int, input().split())) for _ in range(n)]

# move = [[0,1],[1,0]]
# dp = [[0]*301 for _ in range(301)]

# def dfs(x, y, cnt):
#     if x == n-1 and y == m-1:
#         dp[x][y] = max(dp[x][y], maze[x][y] + cnt)
#         return 0
#         # return dp[x][y]

#     if dp[x][y] != 0 and dp[x][y] >= cnt + maze[x][y]:
#         # return dp[x][y]
#         return 0
    
#     dp[x][y] = maze[x][y] + cnt

#     for i, j in move:
#         if x+i < n and y+j < m:
#             dfs(x+i, y+j, dp[x][y])

# dfs(0, 0, 0)
# print(dp[n-1][m-1])

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

move = [[0,1],[1,0]]
dp = [[0]*m for _ in range(n)]

def dfs(x, y, cnt):
    if x == n-1 and y == m-1:
        dp[x][y] = max(dp[x][y], maze[x][y] + cnt)
        return 0
        # return dp[x][y]

    if dp[x][y] != 0 and dp[x][y] >= cnt + maze[x][y]:
        # return dp[x][y]
        return 0
    
    dp[x][y] = maze[x][y] + cnt

    for i, j in move:
        if x+i < n and y+j < m:
            dfs(x+i, y+j, dp[x][y])

dfs(0, 0, 0)
print(dp[n-1][m-1])