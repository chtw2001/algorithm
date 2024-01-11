# 2번
import sys
input = sys.stdin.readline

N = int(input())
init = int(input())
ary = [int(input()) for _ in range(N)]

answ = 0
for next in ary:
    a = 360 - max(init, next) + min(init, next)
    b = max(init, next) - min(init, next)
    answ += min(a, b)
    init = next
    
print(answ)