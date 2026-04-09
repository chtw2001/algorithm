# 4번 서울의 지하철

from collections import deque, defaultdict
import sys
input = sys.stdin.readline
N = int(input())
train = dict()
station = defaultdict(list)
start_point = []
visited = [0]*(N+1)

for i in range(1, N+1):
    train[i] = list(map(int, input().split()))
    if 0 in train[i]:
        start_point.append(i)
    elif len(train[i][1:]) != len(set(train[i][1:])):
        continue # cycle
    
    for j in range(train[i][0]):
        station[train[i][j+1]].append(i)
        
destination = int(input())

q = deque()
for t_ in start_point:
    visited[t_] = 1
    for s_ in train[t_][1:]:
        q.append((s_, 0))


while q:
    s, cnt = q.popleft()
    if s == destination:
        print(cnt)
        quit()
    
    for t_ in station[s]:
        if visited[t_]:
            continue
        for s_ in train[t_][1:]: 
            q.append((s_, cnt+1)) 
        
        visited[t_] = 1

print(-1)
