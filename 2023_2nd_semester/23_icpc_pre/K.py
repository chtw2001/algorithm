import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
ary = [list(map(int, input().split())) for _ in range(N)]
answ = defaultdict(int)
for x, y in ary:
    answ[(x, y)] += 1

order = 0
while order < N:
    x, y = map(int, ary[order])
    for r, c in ary[order+1:]:
        answ[((x+r)/2, (y+c)/2)] += 2
    order += 1

print(max(answ.values()))