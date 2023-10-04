import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(str, input().strip())) for _ in range(n)]
answ = 0

def check(maze, x, y, move):
    global answ
    if move == 'row':
        up, down = 0, 0
        for i in range(y, m-1):
            if maze[x][i] == '.':
                if maze[x-1][i] == 'X':
                    if up:
                        answ += 1
                        up = 0
                    else:
                        up = 1
                else:
                    up = 0
                
                if maze[x+1][i] == 'X':
                    if down:
                        answ += 1
                        down = 0
                    else:
                        down = 1
                else:
                    down = 0
            else:
                up, down = 0, 0
    else:
        left, right = 0, 0
        for i in range(x, n-1):
            if maze[i][y] == '.':
                if maze[i][y-1] == 'X':
                    if left:
                        answ += 1
                        left = 0
                    else:
                        left = 1
                else:
                    left = 0
                
                if maze[i][y+1] == 'X':
                    if right:
                        answ += 1
                        right = 0
                    else:
                        right = 1
                else:
                    right = 0
            else:
                left, right = 0, 0

move = 'row'
for i in range(1, n-1):
    check(maze, i, 1, move) 
    
move = 'column'
for i in range(1, m-1):
    check(maze, 1, i, move) 

print(answ)