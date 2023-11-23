from collections import deque, defaultdict
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(R)] # 
meet = [[0]*C for _ in range(R)] # meet count. if 3: candidate
least_cnt = [[0]*C for _ in range(R)] # sum of each enemy's distance

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
X1 = list(map(int, input().split()))
X2 = list(map(int, input().split()))
X3 = list(map(int, input().split()))

answ_dict = defaultdict(int)

def bfs(x, y):
    visited = [[0]*C for _ in range(R)]
    q = deque()
    q.append((x, y, 0))
    while q:
        a, b, cnt = q.popleft()
        visited[a][b] = 1
        meet[a][b] += 1
        least_cnt[a][b] = max(least_cnt[a][b], cnt)
        for i, j in move:
            dx, dy = a+i, b+j
            if 0 <= dx < R and 0 <= dy < C and not visited[dx][dy] and not maze[dx][dy]:
                q.append((dx, dy, cnt+1))
                visited[dx][dy] = 1

bfs(X1[0]-1, X1[1]-1)
bfs(X2[0]-1, X2[1]-1)
bfs(X3[0]-1, X3[1]-1)

answ = []
for i in range(R):
    for j in range(C):
        if meet[i][j] == 3:
            answ.append(least_cnt[i][j]) # location which 

if not answ:
    print(-1)
else:
    min_cnt = min(answ)
    print(min_cnt)
    print(answ.count(min_cnt))
