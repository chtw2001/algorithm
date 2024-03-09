import sys
input = sys.stdin.readline
sys.setrecursionlimit(200003)
N = int(input())
ary = list(map(int, input().split()))
ary.append(0)
ary.append(0)
dp = [sys.maxsize]*N

def topDown(idx):

    if idx >= N: # ary에 추가한 배열이면 0
        return 0
    if dp[idx] != sys.maxsize:
        return dp[idx]
    dp[idx] = -sys.maxsize
    dp[idx] = max(dp[idx], ary[idx] + topDown(idx+1))
    dp[idx] = max(dp[idx], (ary[idx] + ary[idx+1] + ary[idx+2])*2 + topDown(idx+3))
    return dp[idx]

print(topDown(0))
