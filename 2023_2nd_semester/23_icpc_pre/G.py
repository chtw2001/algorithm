import math
from fractions import Fraction
N, order = map(int, input().split())

answ = {(0, 1), (1, 1)}

for i in range(N, 1, -1):
    for j in range(1, i):
        g = math.gcd(j, i)
        answ.add((j//g, i//g))

sorted_list = sorted(list(answ), key=lambda x: Fraction(x[0], x[1]))
print(sorted_list[order-1][0], sorted_list[order-1][1])