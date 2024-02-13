# 4번 바이러스 복제

before = list(input().rstrip())
after = list(input().rstrip())
N = len(before)
M = len(after)

start, foward = 0, 0
while start <= min(N, M):
    if start == min(N, M):
        break
    if before[start] == after[start]:
        start += 1
        foward = start
        continue
    break

start, backward = -1, -1
while -(min(N, M)) < start:
    if before[start] == after[start]:
        start -= 1
        backward = start
        continue
    break

if foward > min(N, M) + backward:
    if N > M:
        print(0)
    else:
        print(abs(N - M))
else:
    print(M+backward-foward+1)
