# 스티커
import sys
input = sys.stdin.readline

T = int(input())
while T:
    N = int(input())
    sticker = [[] for _ in range(2)]
    for i in range(2):
        sticker[i] = list(map(int, input().split()))
        sticker[i].insert(0, 0)
    
    dp = [[0]*(N+1) for _ in range(2)]
    dp[0][1] = sticker[0][1] # 좌상단 시작
    dp[1][1] = sticker[1][1] # 좌하단 시작
    
    for i in range(2, N+1):
        dp[(i+1)%2][i] = max(dp[i%2][i-1], dp[i%2][i-2]) + sticker[(i+1)%2][i]
        dp[i%2][i] = max(dp[(i+1)%2][i-1], dp[(i+1)%2][i-2]) + sticker[i%2][i]

    print(max(dp[0][-1], dp[1][-1]))
    
    T -= 1
