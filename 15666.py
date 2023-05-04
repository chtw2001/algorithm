import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ex = list(map(int, input().split()))
ex2 = set()
for i in ex:
    ex2.add(i)

maze = []
for i in ex2:
    maze.append(i)

maze.sort()

def check(idx, cnt, q, ex):
    if cnt == m:
        for i in q:
            print(i, end=' ')
        print()
    else:
        for i in range(idx, len(maze)):
            if ex <= maze[i]:
                q.append(maze[i])
                check(i, cnt+1, q, maze[i])
                q.pop()

for i in range(len(maze)):
    q = [maze[i]]
    # idx for maze, recursion count, queue for print, past num
    check(i, 1, q, maze[i]) 