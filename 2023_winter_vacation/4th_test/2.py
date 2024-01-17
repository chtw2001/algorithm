import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ary = [int(input()) for _ in range(N)]

i, cnt = 0, 1
while N:
    if ary[i] == i:
        print(-1)
        quit()
        
    if ary[i] == K:
        print(cnt)
        quit()
    i = ary[i]   
    cnt += 1
    
    N -= 1

print(-1)