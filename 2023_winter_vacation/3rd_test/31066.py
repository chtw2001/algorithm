# 3번
import sys
input = sys.stdin.readline
T = int(input()) # <= 1000

while T:
    N, M, K = map(int, input().split()) # <= 10
    if N != 1 and M == 1 and K == 1:
        print(-1)
        T -= 1
        continue
    
    ex = N
    cnt = 0
    while ex:
        ex -= M*K # 오른쪽으로 가기
        cnt += 1 # count + 1
        if ex <= 0: # 왼쪽 사람 없으면 종료
            break
        ex += 1 # 오른쪽 사람1명이 모든 우산 챙겨서 왼쪼 가기
        cnt += 1 # count + 1
    
    print(cnt)
    T -= 1
    