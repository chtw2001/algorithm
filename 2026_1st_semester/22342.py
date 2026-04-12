import sys
input = sys.stdin.readline

M, N = map(int, input().split())
ary = [list(map(int, list(input().rstrip()))) for _ in range(M)]
output = [[0]*N for _ in range(M)]
save = [[0]*N for _ in range(M)]

for i in range(M):
    output[i][0] = ary[i][0]

for j in range(1, N):
    for i in range(M):
        save[i][j] = max(output[max(0,i-1)][j-1], output[i][j-1], output[min(M-1,i+1)][j-1])
        output[i][j] = save[i][j] + ary[i][j]

answ = 0
for i in range(M):
    for j in range(N):
        answ = max(answ, save[i][j])

print(answ)