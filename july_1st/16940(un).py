from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
dict = defaultdict(list)
for _ in range(n-1):
    s, e = map(int, input().split())
    dict[s].append(e)


quest = list(map(int, input().split()))
psum = [quest[0]]
for i in range(1, n):
    psum.append(psum[i-1]+quest[i])

q = deque()
q.append((1, 0))
# d = [0]*(n+1)
bridge = 1
sum = 1
idx = 0
while q:
    # if not d[bridge]:
    #     bridge += 1
    ex = q.popleft()
    # d[bridge] -= 1
    print(psum[idx], sum)
    if ex[1] != bridge:
        if psum[idx] != sum:
            print(0)
            quit()
        else:
            bridge += 1
        
    for i in dict[ex[0]]:
        idx += 1
        # d[bridge] += 1
        sum += i
        q.append((i, bridge))

print(1)