import sys
input = sys.stdin.readline

N, K = map(int, input().split())
P = list(map(int, input().split()))
P.insert(0, 0)
D = list(map(int, input().split()))
D.insert(0, 0)
# time complexity O(K*N) => 10^7
for _ in range(K):
    ex = [0]*(N+1)
    for i in range(1, N+1):
        ex[D[i]] = P[i]
    
    P = ex

for i in P[1:]:
    print(i, end=' ')