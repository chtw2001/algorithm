# 3번
import sys
input = sys.stdin.readline
T = int(input())

while T:
    N, M, K = map(int, input().split())
    if N != 1 and M == 1 and K == 1:
        print(-1)
        T -= 1
        continue
    
    ex = N
    cnt = 0
    while ex:
        ex -= M*K
        cnt += 1
        if ex <= 0:
            break
        ex += 1
        cnt += 1
    
    print(cnt)
    T -= 1
    