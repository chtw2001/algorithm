N = int(input())
move = ((1, 2), (2, 1))
board = [[0]*N for _ in range(N)]

answ = 0
def check(x, y, cnt):
    global answ
    flag = []
    if not board[x][y]:
        if cnt + 1 == N:
            answ += 1
            return
        board[x][y] = 1
        flag.append((x, y))
    else:
        return
    
    for i in range(N):
        
        if not board[x][i]:
            flag.append((x, i))
        if not board[i][y]:
            flag.append((i, y))
        
        board[x][i] = 1
        board[i][y] = 1
    
    for i in range(N):
        if x + i >= N or y - i < 0:
            break
        if not board[x+i][y-i]:
            flag.append((x+i, y-i))
        
        board[x+i][y-i] = 1
    
    for i in range(N):
        if x - i < 0 or y + i >= N:
            break
        if not board[x-i][y+i]:
            flag.append((x-i, y+i))
        
        board[x-i][y+i] = 1

    for i in range(N):
        if x + i >= N or y + i >= N:
            break
        if not board[x+i][y+i]:
            flag.append((x+i, y+i))
        
        board[x+i][y+i] = 1
    
    for i in range(N):
        if x - i < 0 or y - i < 0:
            break
        if not board[x-i][y-i]:
            flag.append((x-i, y-i))
        
        board[x-i][y-i] = 1

    for i, j in move:
        if (y+j) // N and not N % 2 and j == 2:
            if x + i >= N:
                continue           
            check(x+i, N-1-y, cnt+1)
        elif (x+i) // N and not N % 2 and i == 2:
            if y + j >= N:
                continue
            check(N-1-x, y+j, cnt+1)
        else:
            check((x+i)%N, (y+j)%N, cnt+1)
    
    for i, j in flag:
        board[i][j] = 0
    
    return

for i in range(N):
    # print(board)
    check(0, i, 0)
print(answ)