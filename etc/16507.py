# 1000*1000 배열에서 10,000번 반복하면 무조건 시간초과
# presum을 통해 최대 10,000번의 계산을 빠르게 할 수 있을듯?
import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(r)]
pre_maze = []
for i in range(r):
    ex = [0]*(c+1)
    for j in range(c):
        ex[j+1] = ex[j] + maze[i][j]
    pre_maze.append(ex) # 원래는 ex[1:]로 하려고 했지만, 15번이후 행부터
                        # 0이 들어오면 예외처리를 해주어야해서 그냥 맨 앞 값 => 0

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    size = (r2-r1+1)*(c2-c1+1)
    answ = 0
    for i in range(r1-1, r2):
        answ += pre_maze[i][c2] - pre_maze[i][c1-1]
    print(answ // size)