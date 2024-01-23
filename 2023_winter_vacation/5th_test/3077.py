# 2번 임진왜란

import sys
input = sys.stdin.readline

N = int(input())
battle = list(map(str, input().rstrip().split()))
test = list(map(str, input().rstrip().split()))

dict = dict()
for i in range(N):
    dict[battle[i]] = i
    
answ = 0
for i in range(N):
    for j in range(i+1, N):
        if dict[test[i]] < dict[test[j]]:
            answ += 1

print(f'{answ}/{int(N*(N-1)/2)}')