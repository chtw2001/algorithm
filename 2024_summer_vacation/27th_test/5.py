import sys
input = sys.stdin.readline

tc = 1
move = [(-1, 1), (0, -1), (-1, -1), (-1, 0)] # row, col
while True:
    N = int(input())
    if not N:
        break
    
    ary = [list(map(int, input().split())) for _ in range(N)]
    dp = [[sys.maxsize for _ in range(3)] for _ in range(N)]

    dp[0][1] = ary[0][1]
    dp[0][2] = dp[0][1] + ary[0][2]
    
    for i in range(1, N):
        for j in range(3):
            for x, y in move:
                dx, dy = i+x, j+y
                if dx < 0 or dx >= N or dy < 0 or dy >= 3 or (dx == 0 and dy == 0):
                    continue
                dp[i][j] = min(dp[i][j], dp[dx][dy]+ary[i][j])
    
    print(f'{tc}. {dp[N-1][1]}')
    
    tc += 1
