# 4번 구슬게임
b1, b2, b3 = map(int, input().split())
TC = [list(map(int, input().split())) for _ in range(5)]
dp = [[-1]*501 for _ in range(501)]

def check(a, b):
    if dp[a][b] >= 0:
        return dp[a][b]
    for num in [b1, b2, b3]:
        if a - num >= 0 and not check(a-num, b):
            dp[a][b] = 1
            return 1
    for num in [b1, b2, b3]:
        if b - num >= 0 and not check(a, b-num):
            dp[a][b] = 1
            return 1
    
    dp[a][b] = 0
    return 0

for a, b in TC:
    if check(a, b):
        print('A')
    else:
        print('B')

# 참고: https://ji-gwang.tistory.com/438
