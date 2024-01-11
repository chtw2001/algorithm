from collections import deque
N, K = map(int, input().split())

if N >= K:
    print(abs(K-N))
    quit()

visited = [0]*100001
q = deque()
q.append((N, 0))

while q:
    p, num = q.popleft()
    
    if visited[p]:
        continue
    
    visited[p] = 1
    
    if p == K:
        print(num)
        break
    
    for new_p in [p+1, p-1]:
        if 0 <= new_p <= 100000 and not visited[new_p]:
            q.append((new_p, num+1))

    if 0 <= 2*p <= 100000 and not visited[2*p]: # appendleft when zero weight
        q.append((2*p, num))
