import sys
from collections import defaultdict
input = sys.stdin.readline

N, W = map(int, input().split())
cnt_3, cnt_5 = [], []
num_3, num_5 = 0, 0
for _ in range(N):
    num, sweet = map(int, input().split())
    if num == 3:
        cnt_3.append(sweet)
        num_3 += 1
    else:
        cnt_5.append(sweet)
        num_5 += 1

cnt_3.sort(reverse=True)
cnt_5.sort(reverse=True)

psum_3 = [0]
ex = 0
for i in range(num_3):
    ex += cnt_3[i]
    psum_3.append(ex)

psum_5 = [0]
ex = 0
for i in range(num_5):
    ex += cnt_5[i]
    psum_5.append(ex)

answ = -1
three = min(num_3, W // 3)
while three >= 0:
    five = (W - three*3)//5
    if five >= 0:
        answ = max(answ, psum_3[three] + psum_5[min(five, num_5)])
    else:
        answ = max(answ, psum_3[three])
    three -= 1

print(answ)