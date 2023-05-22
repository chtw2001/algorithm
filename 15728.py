import sys

n, k = map(int, input().split())
share = sorted(list(map(int, input().split())))
team = sorted(list(map(int, input().split())))

for _ in range(k):
    answ = -sys.maxsize
    ex = 0
    for i in range(len(share)):
        for j in range(len(team)):
            if share[i]*team[j] > answ:
                answ = share[i]*team[j]
                ex = j
    del team[ex]

answ = -sys.maxsize
for i in share:
    for j in team:
        answ = max(answ, i*j)

print(answ)