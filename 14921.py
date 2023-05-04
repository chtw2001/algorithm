import sys
input = sys.stdin.readline

n = int(input())
maze = list(map(int, input().split()))

if n == 2:
    print(maze[0] + maze[1])
    quit()

start, end = 0, n-1
answ = maze[start] + maze[end]

while start != end:
    ex = maze[start] + maze[end]
    if ex < 0:
        start += 1
    else:
        end -= 1
    if abs(answ) > abs(ex):
        answ = ex
    if answ == 0:
        print(0)
        quit()
    
print(answ)