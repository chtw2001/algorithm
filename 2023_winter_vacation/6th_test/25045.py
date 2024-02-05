# 2번 비즈마켓
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
goods = list(map(int, input().split()))
company = list(map(int, input().split()))

goods.sort(reverse=True) # 2*10^5 * log(2*10^5)
company.sort() # 2*10^5 * log(2*10^5)

sum = 0
for i in range(min(N, M)): # O(min(N, M) => O(2*10^5)
    if goods[i] - company[i] > 0:
        sum += goods[i] - company[i]

print(sum)