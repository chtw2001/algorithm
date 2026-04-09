# 트리의 지름
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10001)

N = int(input())
ary = defaultdict(list)
for _ in range(N-1):
    p, c, v = map(int, input().split())
    ary[p].append([c, v])
    ary[c].append([p, v])

def check(node, cost):
    for n, c in ary[node]:
        if visited[n]:
            continue
        visited[n] = 1
        check(n, c+cost)
    check_ary[node] = cost

visited = [0]*(N+1)
check_ary = [0]*(N+1)
check(1, 0)

s = check_ary.index(max(check_ary))
visited = [0]*(N+1)
check_ary = [0]*(N+1)
check(s, 0)
print(max(check_ary))
