# 파티
# N개의 마을에 사는 사람들이 M개의 단방향 경로로 X까지 갔다가 다시 집으로 돌아가는 최장거리 출력
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M, X = map(int, input().split())
dict = defaultdict(list)
for i in range(M):
    pass

ary = [list(map(int, input().split())) for _ in range(M)]
answ_ary = [0]*N

def dfs(arrive, cost):
    if min_cost <= cost:
        return min_cost
    if arrive == X:
        min_cost = cost
        return cost
    
    visited[arrive] = 1
    for town in 
    dfs()
    visited[arrive] = 0

for i in range(N):
    min_cost = sys.maxsize
    visited = [0]*N
    # visited[i] = 1
    answ_ary[i] = dfs(i, 0)