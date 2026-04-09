# 파티
# N개의 마을에 사는 사람들이 M개의 단방향 경로로 X까지 갔다가 다시 집으로 돌아가는 최장거리 출력
import sys
from collections import defaultdict
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

N, M, X = map(int, input().split())
dict_correct = defaultdict(dict)
dict_reverse = defaultdict(dict)
for i in range(M):
    s, e, cost = map(int, input().split())
    dict_correct[s-1][e-1] = cost
    dict_reverse[e-1][s-1] = cost
    

def shortestPath(start, dict): # 출발지, 목적지
    ary = [sys.maxsize]*N # [idx]에서부터 각 노드 까지의 거리
    ary[start] = 0
    q = [(0, start)]
    while q:
        cost, point = pop(q)
        if ary[point] < cost: # 이미 갱신이 되었으면
            continue
        
        for point_, cost_ in dict[point].items():
            ex = cost + cost_
            
            if ary[point_] > ex:
                ary[point_] = ex
                push(q, (ex, point_))
    
    return ary

ary_correct = shortestPath(X-1, dict_correct)
ary_reverse = shortestPath(X-1, dict_reverse)

answ = -1
for i in range(N):
    if i == X-1:
        continue
    answ = max(answ, ary_correct[i] + ary_reverse[i])

print(answ)
