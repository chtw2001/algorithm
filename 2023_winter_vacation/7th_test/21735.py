# 2번 눈덩이 굴리기
from collections import deque

N, M = map(int, input().split())
ary = list(map(int, input().split()))
ary.insert(0, 0)
q = deque()
q.append((1, 0, 0))

answ = -1
while q:
    size, pos, time = q.popleft()
    if time == M:
        answ = max(answ, size)
        continue

    if pos + 1 <= N:
        q.append((size+ary[pos+1], pos+1, time+1))
    else:
        answ = max(answ, size)

    if pos + 2 <= N:
        q.append((size//2+ary[pos+2], pos+2, time+1))
    else:
        answ = max(answ, size)

print(answ)