# 3번 유성
import sys
input = sys.stdin.readline
print = sys.stdout.write

R, S = map(int, input().split())
picture = [list(input().rstrip()) for _ in range(R)]
metor = [-R]*S
land = [R]*S

for i in range(R):
    for j in range(S):
        if picture[i][j] == 'X':
            metor[j] = max(metor[j], i)
        elif picture[i][j] == '#':
            land[j] = min(land[j], i)

max_metor = max(metor)

down = 0
for i in range(R):
    flag = 0
    for j in range(S):
        metor[j] += 1
    down += 1
    for j in range(S):
        if metor[j] + 1 == land[j]:
            flag = 1
            break
    if flag:
        break

for i in range(max_metor, -1, -1):
    for j in range(S):
        if picture[i][j] == 'X':
            picture[i+down][j] = 'X'
            picture[i][j] = '.'

for i in range(R):
    for j in range(S):
        print(picture[i][j])
    print('\n')
