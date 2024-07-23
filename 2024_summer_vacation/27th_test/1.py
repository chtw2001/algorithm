import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
ary = [int(input()) for _ in range(N)]
q = [int(input()) for _ in range(Q)]

answ = []
for i in range(N):
    for j in range(ary[i]):
        answ.append(i+1)

for i in q:
    print(answ[i])
