import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(N)]

def check(list_k, n):
    ex = -1
    if n == 1:
        for i in range(N):
            ex = max(ex,
                    abs(ary[i][0] - list_k[0][0]) + abs(ary[i][1] - list_k[0][1]))
    elif n == 2:
        for i in range(N):
            ex = max(ex, 
                    min(abs(ary[i][0] - list_k[0][0]) + abs(ary[i][1] - list_k[0][1]),
                        abs(ary[i][0] - list_k[1][0]) + abs(ary[i][1] - list_k[1][1])))
    else:
        for i in range(N):
            ex = max(ex, 
                    min(abs(ary[i][0] - list_k[0][0]) + abs(ary[i][1] - list_k[0][1]),
                        abs(ary[i][0] - list_k[1][0]) + abs(ary[i][1] - list_k[1][1]),
                        abs(ary[i][0] - list_k[2][0]) + abs(ary[i][1] - list_k[2][1])))

    return ex


k_list = []
answ = sys.maxsize
if K == 1:
    for i in range(N):
        answ = min(answ, check([ary[i]], 1))
elif K == 2:
    for i in range(N):
        for j in range(i+1, N):
            answ = min(answ, check([ary[i], ary[j]], 2))
else:
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                answ = min(answ, check([ary[i], ary[j], ary[k]], 3))

print(answ)
