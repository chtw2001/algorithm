import sys
input = sys.stdin.readline

R, C = map(int ,input().split())
board = []
for _ in range(R):
    board.append(list(map(lambda ex: ord(ex)-65, input())))

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
box = [0]*26

answ = 1
def dfs(x, y, point):
    global answ
    if box[board[x][y]]:
        answ = max(answ, point)
        return

    box[board[x][y]] = 1
    for i, j in move:
        if 0 <= x+i < R and 0 <= y+j < C:
            dfs(x+i, y+j, point+1)
                
    box[board[x][y]] = 0
    answ = max(answ, point)

dfs(0, 0, 0)
print(answ)
