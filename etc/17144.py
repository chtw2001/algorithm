import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
move = [[0,1],[0,-1],[1,0],[-1,0]]
maze = []
cleaner = []
dust = []

def dust_check(map):
    dust = []
    for i in range(r):
        for j in range(c):
            if map[i][j] >= 5:
                dust.append([i, j])
    return dust

def dust_print(map):
    answ = 0
    for i in range(r):
        for j in range(c):
            if map[i][j] > 0:
                answ += map[i][j]
    return answ 

def spread(map, dust):
    dust = dust_check(map)
    plus = []
    for i in range(len(dust)):
        cnt = 0
        if map[dust[i][0]][dust[i][1]] // 5:
            for x, y in move:
                if 0 <= x+dust[i][0] < r and 0 <= y+dust[i][1] < c and map[x+dust[i][0]][y+dust[i][1]] != -1:
                    cnt += 1
                    plus.append([x+dust[i][0], y+dust[i][1], map[dust[i][0]][dust[i][1]] // 5]) # [x, y퍼질 미세먼지의 양]

        plus.append([dust[i][0], dust[i][1], -(map[dust[i][0]][dust[i][1]] // 5)*cnt])

    # 확산된 미세먼지는, 모든 위치에서의 확산이 끝나고 더함
    for i, j, num in plus:
        map[i][j] += num

def clean(map, cleaner):
    up, down = cleaner[0], cleaner[1]
    tmp = 0
    for i in range(1, c):
        tmp, map[up[0]][i] = map[up[0]][i], tmp
    for i in range(up[0]-1, -1, -1):
        tmp, map[i][-1] = map[i][-1], tmp
    for i in range(c-2, -1, -1):
        tmp, map[0][i] = map[0][i], tmp
    for i in range(1, up[0]):
        tmp, map[i][0] = map[i][0], tmp
    
    tmp = 0
    for i in range(1, c):
        tmp, map[down[0]][i] = map[down[0]][i], tmp
    for i in range(down[0]+1, r):
        tmp, map[i][-1] = map[i][-1], tmp
    for i in range(c-2, -1, -1):
        tmp, map[-1][i] = map[-1][i], tmp
    for i in range(r-2, down[0], -1):
        tmp, map[i][0] = map[i][0], tmp

for i in range(r):
    ex = list(map(int, input().split()))
    for j in range(c):
        if ex[j] == -1:
            cleaner.append([i, j])  # 청소기 위치
        elif ex[j] >= 5:
            dust.append([i, j])  # 확산될 수 있는 먼지 위치
    maze.append(ex)  # 현재 보드판 생성

for _ in range(t):
    ex = spread(maze, dust)
    clean(maze, cleaner)
    dust = dust_check(maze)

print(dust_print(maze))