n = int(input())
ary = list(map(int, input().split()))

answ = 0
for i in range(3):
    if n < ary[i]:
        answ += n
    else:
        answ += ary[i]
print(answ)