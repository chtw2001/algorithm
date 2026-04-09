import sys
input = sys.stdin.readline

n, m = map(int, input().split())
man = [0]*n

skill = list(map(int, input().split()))
for i in range(n):
    man[i] = skill[i]

v = list(map(int, input().split()))

ex = man[:m]
ex.sort()
del ex[v[0]-1]
times = 1
for i in range(m, n):
    ex.append(man[i])
    ex.sort()
    del ex[v[times]-1]
    times += 1

for i in sorted(ex):
    print(i)