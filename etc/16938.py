import sys
input = sys.stdin.readline

n, l, r, x = map(int, input().split())
maze = list(map(int, input().split()))

key = []
for i in range(n):
    key.append(pow(2, i))

answ = 0
for i in range(1 << n):
    ex = []
    for j in range(n):
        if i & key[j]:
            ex.append(maze[j])

    if len(ex) < 2:
        continue
    sum_ex = sum(ex)
    if sum_ex < l:
        continue
    if sum_ex > r:
        continue
    if max(ex) - min(ex) < x:
        continue
    answ += 1

print(answ)