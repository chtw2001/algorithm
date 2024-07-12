import sys
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))

answ = -1
ex = 0
set = set()
for i in range(2*N):
    if ary[i] in set:
        ex -= 1
    else:
        ex += 1
        set.add(ary[i])
        answ = max(answ, ex)

print(answ)
