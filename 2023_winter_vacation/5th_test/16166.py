# 4번 서울의 지하철

from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
station = defaultdict(list)
train = defaultdict(list)

for train_ in range(1, N+1):
    ex = list(map(int, input().split()))
    train[train_] = ex # [num, s1, s2, s3...]
    for station_ in ex[1:]:
        station[station_].append(train_)


destination = int(input())
t_visited = [0]*(N+1)


def dfs(t, s, cnt, s_cnt):
    if s == destination:
        print(cnt)
        quit()
    t_visited[t] = 1
    for s_ in train[t][1+s_cnt:]:
        if s_ != s:
            dfs(t, s_, cnt, s_cnt+1)
    
    for t_ in station[s]:
        if not t_visited[t_]:
            dfs(t_, s, cnt+1, 0)

dfs(station[0][0], 0, 0, 0)
print(-1)