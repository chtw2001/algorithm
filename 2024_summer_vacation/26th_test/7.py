import sys
input = sys.stdin.readline

ary = [] # [0] => 백 
         # [1] => 흑

while True:
    try:
        ary.append(list(map(int, input().split())))
    except:
        break

N = len(ary)
dp = [[[0]*15 for _ in range(15)] for _ in range(N)]

def check(i, a, b):
    if i >= N or a >= 15 or b >= 15:
        return 0
    else:
        if dp[i][a][b]:
            return dp[i][a][b]
    ex = 0        
    ex = max(ex, check(i+1, a+1, b) + ary[i][0])
    ex = max(ex, check(i+1, a, b+1) + ary[i][1])
    ex = max(ex, check(i+1, a, b))

    return dp[i][a][b] + ex

print(check(0, 0, 0))
