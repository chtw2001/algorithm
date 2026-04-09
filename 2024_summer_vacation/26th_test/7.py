import sys
input = sys.stdin.readline

ary = [] # [0] => 백 
         # [1] => 흑

while True:
    try:
        ex = list(map(int, input().split()))
        if not ex:
            raise
        ary.append(ex)
    except:
        break

N = len(ary)
dp = [[[0]*16 for _ in range(16)] for _ in range(N)]

def check(i, a, b):
    if i == N:
        return 0
    else:
        if dp[i][a][b]:
            return dp[i][a][b]

    if a < 15:
        dp[i][a][b] = max(dp[i][a][b], check(i+1, a+1, b) + ary[i][0])
    if b < 15:
        dp[i][a][b] = max(dp[i][a][b], check(i+1, a, b+1) + ary[i][1])
    
    dp[i][a][b] = max(dp[i][a][b], check(i+1, a, b))
    
    return dp[i][a][b]

print(check(0, 0, 0))
