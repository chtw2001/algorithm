import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# maze = list(map(int, input().split()))
# maze.sort()

def check(idx, cnt, q, ex):
    if cnt == m:
        for i in q:
            print(i, end=' ')
        print()
    else:
        for i in range(idx, n+1):
            if ex <= i:
                q.append(i)
                check(i, cnt+1, q, i)
                q.pop()

for i in range(1, n+1):
    q = [i]
    # idx for maze, recursion count, queue for print, past num
    check(i, 1, q, i) 