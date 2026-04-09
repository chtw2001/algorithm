from collections import deque
N, K = map(int, input().split())

if N >= K:
    print(abs(K-N))
    print(1)
    quit()

visited = [0]*100001
q = deque()
q.append(N)
cnt = 0

while q:
    ex = q.popleft()

    if ex == K:
        cnt += 1
        continue

    ary = [ex-1, ex+1, ex*2]
    for i in ary:
        if 0 <= i < 100001:
            if not visited[i] or visited[i] >= visited[ex]+1:
                visited[i] = visited[ex] + 1
                q.append(i)

print(visited[K])
print(cnt)