# 1번 숫자게임
import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline
N = int(input())
ary = [list(map(int, input().split())) for _ in range(N)]

q = []
for i in range(N):
    ex = -1
    for a in range(5):
        for b in range(5):
            for c in range(5):
                if a == b or a == c or b == c:
                    continue
                ex = max(ex, (ary[i][a]+ary[i][b]+ary[i][c])%10)
    
    push(q, (-ex, -i))

print(-pop(q)[1] + 1)
