# 2번
N = int(input())
ary = list(map(int, input().split()))

max_value = max(ary)
idx = ary.index(max_value)
print(sum(ary) + max_value*(N-2))
