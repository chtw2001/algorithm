# 1번
N = int(input())
ary = sorted(list(map(int, input().split())))
visited = [0]*N

i = 0
answ = 0
while i < N:
    if visited[i]:
        i += 1
        continue
    s = ary[i]
    visited[i] = 1
    for j in range(min(i+1, N), N):
        if visited[j]:
            continue
        if s < ary[j]:
            visited[j] = 1
            s = ary[j]
    
    answ += 1
    i += 1
    
print(answ)