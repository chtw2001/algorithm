from collections import deque

A, B = map(int, input().split())

q = deque()
q.append((A, 0))
visited = set()
while q:
    ex, num = q.popleft()
    if ex == B:
        print(num+1)
        quit()
    
    if ex in visited:
        continue
    
    if ex >= B:
        continue
    
    visited.add((ex, num+1))
    
    q.append((ex*2, num+1))
    q.append((ex*10 + 1, num+1))

print(-1)