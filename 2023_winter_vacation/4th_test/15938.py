# 5번
# 더위 피하기

import sys
input = sys.stdin.readline
X, Y = map(int, input().split())
position = (200, 200)
bias = (200 - X, 200 - Y)

mod = pow(10, 9) + 7
T = int(input())

X_, Y_ = map(int, input().split())
home = (X_ + bias[0], Y_ + bias[1])

wall = set()
N = int(input())
for _ in range(N): # 10^5
    x, y = map(int, input().split())
    dx, dy = x + bias[0], y + bias[1]
    if dx < 0 or dx > 400 or dy < 0 or dy > 400:
        continue
    wall.add((dx, dy)) # exist

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dp = [[[-1]*201 for _ in range(401)] for _ in range(401)] # 10^6*2^5 => 3*10^7

def dfs(x, y, time):
    if x == home[0] and y == home[1]:
        return 1
    if abs(home[0] - x) + abs(home[1] - y) > T - time:
        return 0
    if time == T:
        return 0
    
    if 0 <= dp[x][y][time]:
        return dp[x][y][time]
    
    dp[x][y][time] = 0
    
    for x_, y_ in move:
        if 0 < x + x_ < 401 and 0 < y + y_ < 401:
            if (x+x_, y+y_) in wall:
                continue
            
            dp[x][y][time] = (dp[x][y][time] + (dfs(x+x_, y+y_, time+1) % mod)) % mod
    
    return dp[x][y][time]

print(dfs(200, 200, 0))