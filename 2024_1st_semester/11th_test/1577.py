# 4번 도로의 개수
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
warning = [] # (x1, y1, x2, y2)
for _ in range(K):
    a, b, c, d = map(int, input().split())
    warning.append([a, b, c, d])
    warning.append([c, d, a, b])

road = [[0]*(N+1) for _ in range(M+1)]
road[0][0] = 1
def check(current, warn):
    if current == warn:
        return True
    else:
        return False

for i in range(M + 1):
    for j in range(N + 1):
        if j > 0:
            for ex in warning:
                if check([j-1, i, j, i], ex):
                    break
            else:
                road[i][j] += road[i][j-1]
        if i > 0:
            for ex in warning:
                if check([j, i-1, j, i], ex):
                    break
            else:
                road[i][j] += road[i-1][j]
                
print(road[M][N])
