import sys
from heapq import heapify
input = sys.stdin.readline

n = int(input())
dic = {}
answ = 0
for _ in range(n):
    ex = list(map(str, input().split()))
    if ex[0] == '1':
        try:
            if dic[ex[1]]:
                ex2 = []
                for i in ex[3:]:
                    ex2.append(int(i))
                dic[ex[1]].extend(ex2)
        except:
            ex2 = []
            for i in ex[3:]:
                ex2.append(int(i))
            dic[ex[1]] = ex2
    else:
        try:
            if dic[ex[1]]:
                answ += sum(sorted(dic[ex[1]], reverse=True)[:int(ex[-1])])
                print(answ)
        except:
            pass

print(answ)