# 트리의 지름
import sys
from collections import defaultdict
sys.setrecursionlimit(100001)
input = sys.stdin.readline

N = int(input())
ary = defaultdict(list)
for _ in range(N):
    ex = list(map(int, input().split()))
    for i in range(2, len(ex), 2):
        ary[ex[0]].append([ex[i-1], ex[i]])
        ary[ex[i-1]].append([ex[0], ex[i]])


def check(node, cost):
    for n, c in ary[node]:
        if visited[n]:
            continue
        visited[n] = 1
        check(n, cost + c)
    
    check_ary[node] = cost

visited = [0]*(N+1)
check_ary = [0]*(N+1)
check(1, 0)

s = check_ary.index(max(check_ary))
visited = [0]*(N+1)
check_ary = [0]*(N+1)
check(s, 0)

print(max(check_ary))