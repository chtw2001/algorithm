# 3번 폴짝폴짝
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

bridge = list(map(int, input().split()))
S, E = map(lambda x: int(x) - 1, input().split())
visited = [-1]*N

q = deque()
q.append(S)
while q:
    cur = q.popleft()
    for i in range(cur, -1, -bridge[cur]):
        if visited[i] != -1:
            continue
        visited[i] = visited[cur]+1
        if i == E:
            print(visited[i])
            quit()
        q.append(i)
    
    for i in range(cur, N, bridge[cur]):
        if visited[i] != -1:
            continue
        visited[i] = visited[cur]+1
        if i == E:
            print(visited[i])
            quit()
        q.append(i)

print(-1)
