import sys

N, K, M = map(int, input().split())
ary = [int(input()) for _ in range(N)]
min_size = sys.maxsize
array = []

for i in range(N):
    flag = 0
    length = 0
    
    if ary[i] <= K:
        continue
    
    if ary[i] < 2*K:
        length = ary[i] - K
    else:
        length = ary[i] - 2*K

    min_size = min(min_size, length)
    array.append(length)
    

answ = -1
for size in range(min_size, 0, -1):
    ex = 0
    for bap in array:
        ex += bap // size
    if ex >= M:
        print(size)
        quit()

print(-1)