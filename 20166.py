import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]
wanna = [input().strip() for _ in range(k)]

# can move eight directions
# ignore repeated positions
# check the string using DFS
# h => 행, w => 열
move = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

def check(i, key, h, w):
    global answ
    if i == len(key)-1 and maze[h][w] == key[i]:
        answ += 1
        return 0

    if maze[h][w] == key[i]:
        # run to eight directions
        for x, y in move:
            dx, dy = (h+x)%n, (w+y)%m
            if 0 <= dx and 0 <= dy:
                check(i+1, key, dx, dy)
            else:
                if dx < 0 and dy < 0: # both
                    check(i+1, key, n-1, m-1)
                elif dx < 0: # only dx
                    check(i+1, key, n-1, dy)
                else: # only dy
                    check(i+1, key, dx, m-1)
    else:
        return 0
dic = {}
for key in wanna:
    try:
        if dic[key]:
            print(dic[key])
            continue
    except:
        pass
    
    answ = 0
    for i in range(n):
        for j in range(m):
            check(0, key, i, j)
    dic[key] = answ
    print(answ)