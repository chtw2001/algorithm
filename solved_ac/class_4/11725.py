import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

visited = set()
q = deque()
tree = [0]*(N+1)

q.append(1)
while q:
    p = q.popleft()
    for c in graph[p]:
        if c in visited:
            continue
        q.append(c)
        visited.add(c)
        tree[c] = p

for i in range(2, N+1):
    print(tree[i])
        