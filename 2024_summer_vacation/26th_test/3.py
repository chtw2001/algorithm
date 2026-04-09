import sys
N = int(input())
ary = []
set = set()
for _ in range(N):
    ex = int(input())
    set.add(ex)
    ary.append(ex)


answ = 1
for i in set:
    ex = -1
    cnt = 1
    for j in ary:
        if i == j:
            continue
        if ex == j:
            cnt += 1
        else:
            ex = j
            answ = max(answ, cnt)
            cnt = 1
    answ = max(answ, cnt)
    
print(answ)
