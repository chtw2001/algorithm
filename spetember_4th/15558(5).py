import sys
input = sys.stdin.readline

N, K = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(2)]

def dfs(idx):
    if idx >= N:
        print(1)
        quit()

for time in range(N):
    