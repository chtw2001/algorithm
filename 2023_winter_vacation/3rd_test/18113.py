# 4번
N, K, M = map(int, input().split()) # N <= 10^6
ary = [int(input()) for _ in range(N)] # 김밥의 길이를 담아놓은 배열. 각 원소 <= 10^9
array = []
max_length = -1

def check(size):
    slice = 0
    for bap in array:
        slice += bap // size
    
    return slice


for i in range(N):
    flag = 0
    length = 0
    
    if ary[i] <= K:
        continue
    
    if ary[i] < 2*K:
        length = ary[i] - K
    else:
        length = ary[i] - 2*K

    max_length = max(max_length, length)
    array.append(length)
    
s, e = 1, max_length
while s <= e:
    mid = (s + e) // 2
    target = check(mid)
    if target >= M:
        s = mid + 1
    else:
        e = mid - 1

if not e:
    print(-1)
else:
    print(e)