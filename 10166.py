from math import gcd
n, m = map(int, input().split())

maze = [[1]*2001 for _ in range(2001)]
answ = 0
for i in range(n, m+1):
    for j in range(1, i+1):
        gc = gcd(i, j)
        if maze[i//gc][j//gc]:
            maze[i//gc][j//gc] = 0
            answ += 1

print(answ)