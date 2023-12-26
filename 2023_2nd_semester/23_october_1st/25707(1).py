import sys
input = sys.stdin.readline

N = int(input())
maze = list(map(int, input().split()))
answ = [0]*N # O(N)

answ[N-1] = 1
for i in range(N-1, -1, -1):
    if i + 1 + maze[i] < N: # 끝까지 가지 않음 => 다음step + 1
        answ[i] = answ[i + 1 + maze[i]] + 1
    else:
        answ [i] = 1 # 이거 밟으면 끝까지 감 => 1

for i in answ:
    print(i, end=' ')