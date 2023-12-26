from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = deque()
q.append((0, 0, ary[0][0], 1)) # x, y, booster, cnt
visited[0][0] = 1
move = [(1, 0), (0, 1)]


while q:
    x, y, v, cnt = q.popleft()

    for i, j in move:
        for k in range(1, v+1):
            dx, dy = i*k, j*k
            if 0 <= x + dx < N and 0 <= y + dy < M and not visited[x+dx][y+dy]:
                if x+dx == N-1 and y+dy == M-1:
                    print(cnt)
                    quit()
                q.append((x+dx, y+dy, ary[x+dx][y+dy], cnt+1))
                visited[x+dx][y+dy] = 1
