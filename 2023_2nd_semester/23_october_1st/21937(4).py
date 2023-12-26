import sys
input = sys.stdin.readline
sys.setrecursionlimit(100010)

N, M = map(int, input().split()) # O(N) => 10^5 => num of edge 
info = [[] for _ in range(N+1)]
done = [0]*(N+1)

for _ in range(M):
    f, l = map(int, input().split())
    info[l].append(f)

key = int(input())

def dfs(idx):
    answ = 0
    while info[idx]:
        
        ex = info[idx].pop()
        if not done[ex]: # 여러개의 작업이 1개의 작업을 선수 작업으로 요구할 수 있음.
            answ += 1
        done[ex] = 1
        answ += dfs(ex)
    return answ

print(dfs(key))