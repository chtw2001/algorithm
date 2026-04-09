import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]
depth = [0]*n
cost = [0]*n


def dfs(_list, length, idx, d):
    if idx == length:
        depth[idx - 1] = d % 2
        return
    
    if tree[_list[0]]:
        dfs(tree[_list[0]], len(tree[_list[0]]), 0, d+1)
    
    dfs(tree[_list[idx+1]], len(tree[_list[idx+1]]), idx+1, d)

dfs(tree[0], len(tree[0]), 0, 0)
for _ in range(n-1):
    m, s = map(int, input().split())
    tree[m].append(s)

for i in range(n):
    w, b = map(int, input().split())
    cost[i] = [w, b]

odd_w, odd_b, even_w, even_b = 0, 0, 0, 0
for i in range(n):
    if depth[i]:
        even_w += cost[i][0]
        even_b += cost[i][1]
    else:
        odd_w += cost[i][0]
        odd_b += cost[i][1]


print(min(even_w + odd_b, even_b + odd_w))