# 파티
# N개의 마을에 사는 사람들이 M개의 단방향 경로로 X까지 갔다가 다시 집으로 돌아가는 최장거리 출력
import sys
from collections import defaultdict
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

N, M, X = map(int, input().split())
dict_correct = defaultdict(dict)
# dict_reverse = defaultdict(dict)
for i in range(M):
    s, e, cost = map(int, input().split())
    dict_correct[s-1][e-1] = cost
    

def shortestPath(start): # 출발지, 목적지
    ary = [sys.maxsize]*N # [idx]에서부터 각 노드 까지의 거리
    ary[start] = 0
    q = [(0, start)]
    while q:
        cost, point = pop(q)
        if ary[point] < cost: # 이미 갱신이 되었으면
            continue
        
        for point_, cost_ in dict_correct[point].items():
            ex = cost + cost_
            
            if ary[point_] > ex:
                ary[point_] = ex
                push(q, (ex, point_))
    
    return ary

answ = -1
for i in range(N):
    go_to = shortestPath(i)
    come_to = shortestPath(X-1)
    
    answ = max(answ, go_to[X-1] + come_to[i])
    
print(answ)
