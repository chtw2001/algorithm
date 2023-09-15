# 모든 가중치가 1이기 때문에 bfs를 사용할 수 있다.
# 가중치 여러개 => 다익스트라
# 가중치 0, 1 => 0,1 bfs
# DAG => dp
from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

move = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]

q = deque()
visited = [[True]*n for _ in range(n)]
visited[r1][c1] = False
# visited배열에 이동거리를 넣어도 좋아요 => 코드 최적화 가능

# q.append((0,0,0))
# for 문 대신 0,0을 넣어주면 됩니다
for i, j in move:
    if 0 <= r1 + i < n and 0 <= c1 + j < n:
        q.append((r1+i, c1+j, 1))
        if r1+i == r2 and c1+j == c2:
            print(1)
            quit()
        visited[r1+i][c1+j] = False

while q:
    x, y, cnt = q.popleft()
    for i, j in move:
        if 0 <= x + i < n and 0 <= y + j < n and visited[x+i][y+j]:
            if x+i == r2 and y+j == c2:
                print(cnt + 1)
                quit()
            q.append((x+i, y+j, cnt+1))
            visited[x+i][y+j] = False

print(-1)