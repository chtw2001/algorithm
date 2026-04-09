# 4번 태상이의 훈련소 생활
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ary = list(map(int, input().split()))
ary.insert(0, 0)

teacher = [list(map(int, input().split())) for _ in range(M)]
new_ary = [0]*(N+2)
for i in teacher:
    new_ary[i[0]] += i[-1]
    new_ary[i[1]+1] -= i[-1]

for i in range(N+1):
    new_ary[i+1] += new_ary[i]

for i in range(1, N+1):
    ary[i] += new_ary[i]
    
print(*ary[1:])
