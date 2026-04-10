import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = input().strip()

move = [[-1, 0], [1, 0], [0, -1], [0, 1]] # U D L R
pos = [0, 0]

cnt = min(N, K)
i = 0
while (i//N) < cnt:
    idx = i % N
    order = S[idx]
    if order == 'U':
        pos[0] += move[0][0]
        pos[1] += move[0][1]
    elif order == 'D':
        pos[0] += move[1][0]
        pos[1] += move[1][1]
    elif order == 'L':
        pos[0] += move[2][0]
        pos[1] += move[2][1]
    elif order == 'R':
        pos[0] += move[3][0]
        pos[1] += move[3][1]  

    if pos[0] == 0 and pos[1] == 0:
        print("YES")
        quit()

    i += 1

print("NO")