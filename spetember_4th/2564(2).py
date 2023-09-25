import sys
input = sys.stdin.readline

x, y = map(int, input().split())
N = int(input())
# maze = [[0]*(y+1) for _ in range(x+1)]
store = []
def position(_p, _v):
    if _p == 1:
        return [0, _v]
    elif _p == 2:
        return [x, _v]
    elif _p == 3:
        return [_v, 0]
    else:
        return [_v, y]


for _ in range(N):
    p, v = map(int, input().split())
    pp, vv = map(int, position(p, v))
    store.append((pp, vv))

p, v = map(int, input().split()) # position, value
