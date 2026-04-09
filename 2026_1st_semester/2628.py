import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = int(input())
if cnt == 0:
    print(N*N)
    quit()

cut = [list(map(int, input().split())) for _ in range(cnt)]

h, w = [0], [0]

i, h_num, w_num = 0, 2, 2
while i != cnt:
    a, b = cut[i]
    if a == 0:
        w.append(b)
        w_num += 1
    elif a == 1:
        h.append(b)
        h_num += 1

    i += 1

h.sort()
w.sort()
h.append(N)
w.append(M)

answ = 0
for i in range(1, w_num):
    for j in range(1, h_num):
        W = (w[i]-w[i-1])
        H = (h[j]-h[j-1])
        answ = max(answ, W*H)

print(answ)