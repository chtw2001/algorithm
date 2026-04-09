# 2번 물주기
N, K, A, B = map(int, input().split())
leaf = [K]*N

answ = 1
idx = -A
while True:
    idx += A
    idx %= N
    for i in range(idx, idx+A):
        leaf[i] += B
    for i in range(N):
        if not leaf[i] - 1:
            print(answ)
            quit()
        leaf[i] -= 1
    
    answ += 1
