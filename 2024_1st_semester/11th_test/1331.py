# 1번 나이트 투어
import sys
input = sys.stdin.readline

input = [str(input().rstrip()) for _ in range(36)]
board = dict()
row = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(6):
    for j in range(6):
        board[row[i] + str(j+1)] = [(i, j), 0] # position, cache

move = [(2, 1), (1, 2), (-1, -2), (-1, 2), (1, -2), (-2, -1), (-2, 1), (2, -1)]
initial = board[input[0]][0]
init = board[input[0]][0]
board[input[0]][1] = 1

for pos in input[1:]:
    flag = 0
    if not board[pos][1]:
        board[pos][1] = 1
        for x, y in move:
            if init[0] + x == board[pos][0][0] and init[1] + y == board[pos][0][1]:
                flag = 1

        if not flag:
            print("Invalid")
            quit()
    else:
        print("Invalid")
        quit()
    
    init = board[pos][0]

flag = 0
for x, y in move:
    if init[0] + x == initial[0] and init[1] + y == initial[1]:
        flag = 1

if not flag:
    print("Invalid")
    quit()
    
print("Valid")