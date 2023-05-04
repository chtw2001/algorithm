import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

def row(arr):       # check 1bit only row side
    cnt = 0
    for i in range(n):
        ex = ''
        for j in range(m):
            if not arr[i][j]:
                ex += str(maze[i][j])
            else:
                if ex != '':
                    cnt += int(ex)
                    ex = ''
                else:
                    continue
        if ex != '':
            cnt += int(ex)
    return cnt

def column(arr):    # check 0bit only column side
    cnt = 0
    for i in range(m):
        ex = ''
        for j in range(n):
            if arr[j][i]:
                ex += str(maze[j][i])
            else:
                if ex != '':
                    cnt += int(ex)
                    ex = ''
                else:
                    continue
        if ex != '':
            cnt += int(ex)
    return cnt

answ = []
key = []    # 2^0 ~ 2^(m*n-1) graph
_ = 0
for i in range(n):
    ex = []
    for j in range(m):
        ex.append(pow(2, _))
        _ += 1
    key.append(ex)

for i in range(pow(2, n*m)):    # run 2^(m*n) times
    ex = [[0]*m for _ in range(n)]      # made by using array 'key' and variable 'i'
    for j in range(n):
        for k in range(m):
            ex[j][k] = i & key[j][k]
    a = row(ex)
    b = column(ex)
    answ.append(a+b)

print(max(answ))