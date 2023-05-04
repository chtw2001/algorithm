# 설마 최대공약수의 약수?
import math
n, m = map(int, input().split())

num = math.gcd(n, m)

for i in range(1, num//2+1):
    if num % i == 0:
        print(i, n//i, m//i)

print(num, n//num, m//num)