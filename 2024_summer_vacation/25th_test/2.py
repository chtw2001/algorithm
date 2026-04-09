import sys
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))

ex = ary[0]
answ = 0
for i in range(1, N):
    answ += ex * ary[i]
    ex += ary[i]

print(answ)
