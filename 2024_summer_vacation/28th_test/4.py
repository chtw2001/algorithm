import sys
input = sys.stdin.readline

S, C = map(int, input().split())
ary = [int(input()) for _ in range(S)]
ary.sort()

s, e = 1, sys.maxsize
while s <= e:
    mid = (s + e) // 2
    ex = 0
    for i in range(S):
        ex += ary[i] // mid
    
    if ex >= C:
        s = mid + 1
    else:
        e = mid - 1

answ = 0
if e == 1:
    ex = sum(ary)
    print(ex - C)
else:
    print(sum(ary) - (C*e))
