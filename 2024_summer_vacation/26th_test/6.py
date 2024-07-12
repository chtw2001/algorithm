import sys
input = sys.stdin.readline

TC = int(input())

while TC:
    N, M = map(int, input().split())
    dp = [[sys.maxsize]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        dp[x][y] = c
        dp[y][x] = c

    for i in range(1, N+1):
        dp[i][i] = 0
        
    K = int(input())
    room_no = list(map(int, input().split()))

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j or i == k or j == k:
                    continue
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    answ = sys.maxsize
    
    q = []
    for i in range(1, N+1):
        ex = 0
        for j in range(K):
            ex += dp[i][room_no[j]]
        
        q.append([ex, i])
        # answ = min(answ, ex)

    print(sorted(q)[0][1])
    TC -= 1
