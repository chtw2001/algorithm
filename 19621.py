import sys
input = sys.stdin.readline

n = int(input())
maze = []
max_start = 0
for _ in range(n):
    ex = list(map(int, input().split()))
    max_start = max(max_start, ex[0])
    maze.append(ex)

maze.sort()

answ = []
def check(idx, cnt):
    cnt += maze[idx][-1]
    if maze[idx][1] > max_start:
        answ.append(cnt)
        return
    for i in range(idx+1, n):
        if maze[idx][1] <= maze[i][0]:
            check(i, cnt)

for i in range(n):
    check(i, 0)

print(max(answ))