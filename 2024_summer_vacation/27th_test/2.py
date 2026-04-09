import sys
input = sys.stdin.readline

N, M = map(int, input().split())
q = list(map(int, input().split()))
fr = list(map(int, input().split()))

index_list = []
for i in range(M):
    index_list.append(q.index(fr[i]))

answ = 0
for idx in index_list:
    if idx >= M:
        answ += 1
        
print(answ)
