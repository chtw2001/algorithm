import sys
input = sys.stdin.readline

n, m = map(int, input().split())
road = []*(n+1)
for _ in range(m+1):
    s, e, h = map(int, input().split())
    if h:
        h = 0
    else:
        h = 1
    road[s].append([e, h])
    road[e].append([s, h])
    
    