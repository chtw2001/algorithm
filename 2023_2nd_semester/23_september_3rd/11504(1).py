import sys
input = sys.stdin.readline

TC = int(input())

def check(_idx):
    z = 0
    for i in range(M-1, -1, -1):
        z += ary[_idx % N]*pow(10, i)
        _idx += 1

    return z


for _ in range(TC):
    N, M = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x, y = 0, 0
    j = M - 1
    for i in range(M):
        x += x_list[i]*pow(10, j)
        j -= 1
    
    j = M - 1
    for i in range(M):
        y += y_list[i]*pow(10, j)
        j -= 1

    answ = 0
    ary = list(map(int, input().split()))

    for idx in range(N):
        z = check(idx)
        if x <= z <= y:
            answ += 1
    
    print(answ)