# 5번 관악산 등산

import sys
input = sys.stdin.readline
sys.setrecursionlimit(5001)
N, M = map(int, input().split())
height = list(map(int, input().split()))
height.insert(0, 0)
vertex = [[] for _ in range(N+1)]

dp = [0]*(N+1) 
for _ in range(M):
    s, e = map(int, input().split())
    vertex[s].append((height[e], e))
    vertex[e].append((height[s], s))
    
def dfs(node):
    if dp[node]:
        return dp[node]
    v = 1
    for h, n in vertex[node]:
        if height[node] < h:
            ex = dfs(n)
            v = max(v, ex + 1)
    dp[node] = v
    return dp[node]
    
for i in range(1, N+1):
    print(dfs(i))
