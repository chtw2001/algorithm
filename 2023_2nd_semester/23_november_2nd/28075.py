N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(2)]

answ = 0 # M을 넘는 경우

def check(i, j, day, contrib):
    global answ
    if day == N:
        if contrib >= M:
            answ += 1
        return
    for r in range(2):
        for c in range(3):
            if j == c:
                check(r, c, day+1, (contrib+maze[r][c]//2))
            else:
                check(r, c, day+1, contrib+maze[r][c])



for i in range(2):
    for j in range(3):
        check(i, j, 1, maze[i][j]) # x, y, day, conrtib
        
print(answ)
