import sys
input = sys.stdin.readline
N = int(input())
board = [0]*N

def back_tracking(row):
    for i in range(row):
        if board[row] == board[i] or row - i == abs(board[i] - board[row]): # 같은 행에 있나?, 대각선에 있나?
            return 0
    
    return 1

def dfs(row):
    if row == N:
        return 1
    
    answ = 0
    for col in range(N):
        board[row] = col
        if back_tracking(row):
            answ += dfs(row+1)
        
    return answ

print(dfs(0))
