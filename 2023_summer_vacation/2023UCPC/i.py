import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ex = list(map(int, input().split()))
ary = []
for i in range(n):
    ary.append((ex[i], i+1))
ary.sort()

