import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [int(input().strip()) for _ in range(n)]
arr = [0]*(m+1)

for i in range(n):
    if i % 2 == 0 and maze[i] >= 0:
        arr[0] += 1
        arr[maze[i]] -= 1 
    else:
        arr[m-maze[i]] += 1

psum = [0]*m
ex = 0
for i in range(m):
    ex += arr[i]
    psum[i] = ex

m_value = min(psum)
cnt = psum.count(m_value)

print(m_value, cnt)