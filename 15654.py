import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = list(map(int, input().split()))
maze.sort()

def check(idx, cnt, q, ex):
    if cnt == m:
        for i in q:
            print(i, end=' ')
        print()
    else:
        for i in range(n):
            if maze[i] not in q:
                q.append(maze[i])
                check(i, cnt+1, q, maze[i])
                q.pop()

for i in range(n):
    q = [maze[i]]
    # idx for maze, recursion count, queue for print, past num
    check(i, 1, q, maze[i]) 