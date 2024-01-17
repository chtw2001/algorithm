import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [[0] + list(map(int, input().split())) for _ in range(N)]
table.insert(0, [0]*(N+1))

# 1D p_sum
for i in range(1, N+1):
    for j in range(2, N+1):
        table[i][j] += table[i][j-1]


# 2D p_sum
for i in range(2, N+1):
    for j in range(1, N+1):
        table[i][j] += table[i-1][j]


while M:
    x1, y1, x2, y2 = map(int, input().split())
    print((table[x2][y2] + table[x1-1][y1-1]) - (table[x2][y1-1] + table[x1-1][y2]))
    M -= 1