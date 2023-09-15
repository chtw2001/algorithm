maze = [list(map(int, input().split())) for _ in range(4)]

xy = [[0]*101 for _ in range(101)]

for i in maze:
    for j in range(i[1], i[3]):
        for k in range(i[0], i[2]):
            xy[j][k] += 1

cnt = 0
for i in range(101):
    for j in range(101):
        if xy[i][j] > 0:
            cnt += 1

print(cnt)