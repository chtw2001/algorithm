import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def topDownRow(row, idx):
    if idx >= N:
        return 0
    if dp_row[row][idx]:
        return dp_row[row][idx]
    
    dp_row[row][idx] = max(box[row][idx] + topDownRow(row, idx+2), topDownRow(row, idx+1))

    return dp_row[row][idx]

def topDownCol(col, idx):
    if idx >= M:
        return 0
    if dp_col[idx]:
        return dp_col[idx]

    dp_col[idx] = max(dp_row[idx] + topDownCol(col, idx+2), topDownCol(col, idx+1))

    return dp_col[idx]

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        quit()
    box = []
    for _ in range(M):
        box.append(list(map(int, input().split())))
    
    dp_row = [[0]*(N+1) for _ in range(M)]
    for i in range(M):
        dp_row[i] = topDownRow(i, 0)
    
    dp_col = [0]*(M+1)
    print(topDownCol(i, 0))
