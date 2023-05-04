import sys
input = sys.stdin.readline

sub_n, point = map(int, input().split())
maze = [0]*sub_n

for _ in range(sub_n):
    n, m = map(int, input().split())
    ex = list(map(int, input().split()))
    if n < m:
        maze[_] = 1
    else:
        ex.sort()
        maze[_] = ex[-m]

maze.sort()
answ = 0
for i in maze:
    point -= i
    if point < 0:
        break
    answ += 1

print(answ)