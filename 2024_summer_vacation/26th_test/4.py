import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
ary = list(map(int, input().split()))

prime = [0]*3001
prime[1] = 1

prime_set = set()
for i in range(2, 3001):
    if not prime[i]:
        prime_set.add(i)
        for j in range(2*i, 3001, i):
            prime[j] = 1

answ = []
for list_ in combinations(ary, M):
    ex = sum(list_)
    if ex in prime_set:
        answ.append(ex)

if answ:
    print(*sorted(list(set(answ))))
else:
    print(-1)
