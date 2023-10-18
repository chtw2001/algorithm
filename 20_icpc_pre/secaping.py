import sys
input = sys.stdin.readline

N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]
t = list(map(int, input().split()))
flag = True

# n
for i in range(N):
    if t[1] >= p[i][1]:
        continue
    dx, dy = abs(t[0] - p[i][0]), abs(t[1] - p[i][1])
    if dx <= dy:
        flag = False
        break  

if flag:
    print("YES")
    quit()
flag = True

# s
for i in range(N):
    if t[1] <= p[i][1]:
        continue
    dx, dy = abs(t[0] - p[i][0]), abs(t[1] - p[i][1])
    if dx <= dy:
        flag = False
        break

if flag:
    print("YES")
    quit()
flag = True

# e
for i in range(N):
    if t[0] >= p[i][0]:
        continue
    dx, dy = abs(t[0] - p[i][0]), abs(t[1] - p[i][1])
    if dx >= dy:
        flag = False
        break

if flag:
    print("YES")
    quit()
flag = True

# w
for i in range(N):
    if t[0] <= p[i][0]:
        continue
    dx, dy = abs(t[0] - p[i][0]), abs(t[1] - p[i][1])
    if dx >= dy:
        flag = False
        break

if flag:
    print("YES")
    quit()
    
print("NO")
