# 5번
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[sys.maxsize]*501 for _ in range(N+1)]
island = list(map(int, input().split())) # island[n] => n번째 섬의 높이
for i in range(N):
    dp[i+1][0] = island[i]

connect = defaultdict(list) # island의 연결 정보
for _ in range(M):
    s, e = map(int, input().split())
    connect[s].append(e)
    connect[e].append(s)
    
for k in range(1, 501):
    for i in range(1, N+1):
        for ele in connect[i]:
            dp[i][k] = min(dp[i][k], dp[ele][k-1])
            
T = int(input())
while T:
    pos, k = map(int, input().split())
    if dp[pos][k] < sys.maxsize:
        print(dp[pos][k])
    else:
        print(-1)
    
    T -= 1