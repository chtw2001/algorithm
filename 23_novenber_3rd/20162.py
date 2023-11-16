import sys
input = sys.stdin.readline

N = int(input())
ary = [int(input()) for _ in range(N)]
satisfy = ary.copy()
# O(N^2)
for i in range(N):
    for j in range(i):
        if ary[i] > ary[j]: # 더 커야함
            if satisfy[j] + ary[i] > satisfy[i]: # n번 * n번 비교 n(n-1)//2
                satisfy[i] = satisfy[j] + ary[i]

print(max(satisfy)) # n