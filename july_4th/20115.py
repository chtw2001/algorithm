import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int, input().split()))

ary.sort()
for i in range(n-1):
    ary[-1] += ary[i]/2

print(ary[-1])
# 큰걸 쪼개면 오히려 작아져서 작은걸 쪼개서 큰거에 더했더니 맞아버림