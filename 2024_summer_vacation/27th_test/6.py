import sys
input = sys.stdin.readline

input_ = []
visited = [0]*13
order, pre = 0, 0
fill_up = []
for row in range(5):
    ex = list(input().rstrip())
    for i in range(9):
        if ord(ex[i]) <= 64 or ord(ex[i]) > 76:
            if ex[i] == '.':
                continue
            ex[i] = 0
            fill_up.append([row, i])
            continue
        visited[ord(ex[i])-64] = True
        ex[i] = ord(ex[i])-64
        pre += 1
    input_.append(ex)

def check():
    row1 = input_[0][4] + input_[1][3] + input_[2][2] + input_[3][1]
    row2 = input_[1][1] + input_[1][3] + input_[1][5] + input_[1][7]
    row3 = input_[0][4] + input_[1][5] + input_[2][6] + input_[3][7]
    row4 = input_[1][1] + input_[2][2] + input_[3][3] + input_[4][4]
    row5 = input_[1][7] + input_[2][6] + input_[3][5] + input_[4][4]
    row6 = input_[3][1] + input_[3][3] + input_[3][5] + input_[3][7]
    
    if row1 != 26 or row2 != 26 or row3 != 26 or row4 != 26 or row5 != 26 or row6 != 26:
        return False
    
    return True


def res():
    for row in input_:
        for ele in row:
            if ele == '.':
                print(ele, end='')
                continue
            print(chr(ele+64), end='')
        print()


def dfs(cnt):
    global order
    if cnt == 12-pre:
        if check():
            res()
            quit()
        return
    
    for i in range(1, 13):
        if visited[i]:
            continue
        visited[i] = True
        input_[fill_up[order][0]][fill_up[order][1]] = i
        order += 1
        dfs(cnt + 1)
        order -= 1
        visited[i] = False

dfs(0)
