from collections import deque, defaultdict
N, K = map(int, input().split())

if N >= K:
    print(abs(K-N))
    print(1)
    quit()

q = deque()
q.append((N, 0))
visited = set()
answ_dict = defaultdict(int)

while q:
    ex, num = q.popleft()
    if ex == 3 and num ==2 :
        print(1)
    if ex in visited and not answ_dict[num]:
        continue
    
    if ex < 0 or ex > 100000:
        continue
    
    visited.add(ex)
    if ex == K:
        answ_dict[num] += 1
        continue
    
    if ex > K:
        q.append((ex-1, num+1))
        continue
    
    q.append((ex+1, num+1))
    q.append((ex-1, num+1))
    q.append((ex*2, num+1))


answ = 0
for key in sorted(answ_dict.keys()):
    if answ_dict[key]:
        answ = key

print(answ)
print(answ_dict[answ])