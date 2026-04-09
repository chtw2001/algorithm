import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
ary = [list(map(int, input().split())) for _ in range(N)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
answ = sys.maxsize

def bfs(threshold):
    q = deque()
    q.append([0, 0])
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1:
            return threshold
        
        for i, j in move:
            dx, dy = x+i, y+j
            if dx < 0 or dx >= N or dy < 0 or dy >= N \
                or visited[dx][dy] or abs(ary[x][y] - ary[dx][dy]) > threshold:
                continue
            q.append([dx, dy])
            visited[dx][dy] = 1
    
    return -1


start, end = 0, 1000000000
while start <= end:
    mid = (start + end) // 2
    result = bfs(mid)
    if result == -1:
        start = mid + 1
    else:
        end = mid - 1
        
print(start)
