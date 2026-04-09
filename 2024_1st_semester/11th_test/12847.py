# 2번 꿀 아르바이트
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pay = list(map(int, input().split()))

presum_pay = [0]

ex = 0
for i in pay:
    ex += i
    presum_pay.append(ex)

answ = -1
for i in range(N-M+1):
    answ = max(answ, presum_pay[M+i] - presum_pay[i])

print(answ)