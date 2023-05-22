import sys
n = int(input())
maze = [0]*(n+1)
psum = [0]*(n+1)

for _ in range(n):
    v, m = map(int, input().split())
    maze[v] = m
    psum[v] = m + psum[v-1]

for i in range(1, n+1):
    if psum[i] >= psum[n] - psum[i]:
        print(i)
        quit()
