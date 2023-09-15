# import sys
# input = sys.stdin.readline

# n, m, k = map(int, input().split())
# maze = [input().strip() for _ in range(m)]
# answ = input().strip()
# cnt = 0
# dp = [[0]*7 for _ in range(7)]


# def check(x, y, i):
#     global cnt
#     ex = 0
#     for j in range(x-k, x+k+1):
#         if 0 <= j < m and maze[j][y] == answ[i]:
#             if i == len(answ)-1:
#                 cnt += 1
#                 ex += 1
#             elif dp[j][y] != 0:
#                 cnt += dp[j][y]
#                 return 0
#             else:
#                 ex += 1
#                 check(j, y, i+1)
    
#     for j in range(y-k, y+k+1):
#         if 0 <= j < n and maze[x][j] == answ[i]:
#             if i == len(answ)-1:
#                 cnt += 1
#                 ex += 1
#             elif dp[x][j] != 0:
#                 cnt += dp[x][j]
#                 return 0
#             else:
#                 ex += 1
#                 check(x, j, i+1)
#     dp[x][y] += ex
#     return dp[x][y]

# for z in range(m):
#     for j in range(n):
#         if maze[z][j] == answ[0]:
#             dp[z][j] += check(z, j, 1)

# print(cnt)
# print(dp)

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
maze = [input().strip() for _ in range(m)]
answ = input().strip()
cnt = 0

def check(x, y, i):
    global cnt
    for j in range(x-k, x+k+1):
        if 0 <= j < m and maze[j][y] == answ[i]:
            if i == len(answ)-1:
                cnt += 1
            else:
                check(j, y, i+1)
    
    for j in range(y-k, y+k+1):
        if 0 <= j < n and maze[x][j] == answ[i]:
            if i == len(answ)-1:
                cnt += 1
            else:
                check(x, j, i+1)

for k in range(m):
    for j in range(n):
        if maze[k][j] == answ[0]:
            check(k, j, 1)

print(cnt)