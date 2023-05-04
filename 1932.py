# import sys
# input = sys.stdin.readline

# n = int(input())
# maze = [list(map(int, input().split())) for _ in range(n)]

# for i in range(1, n):
#     for j in range(i+1):
#         if j == 0:
#             maze[i][j] += maze[i-1][0] # 9, 11행 =>
#         elif i == j:
#             maze[i][j] += maze[i-1][-1]  # 양 끝은 위에서 받아올게 양 끝 1개씩밖에 없음
#         else:
#             maze[i][j] += max(maze[i-1][j-1], maze[i-1][j]) # 그 외 행은 2개씩

# print(max(maze[n-1]))

# do bottom up 
import sys
input = sys.stdin.readline

n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-2, -1, -1):
    for j in range(i+1):
        maze[i][j] += max(maze[i+1][j], maze[i+1][j+1])

print(maze[0][0])