# 파이프 옮기기 1 
# bfs 시간초과
# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())
# room = [list(map(int, input().split())) for _ in range(N)]
# if room[N-1][N-1] == 1:
#     print(0)
#     quit()

# # move = (x1, y1, x2, y2, status)
# move = [[(0, 1, 0, 1, 0), (0, 1, 1, 1, 2)], # 가로, status [0, 1, 2] => 가로, 세로, 대각선
#         [(1, 0, 1, 0, 1), (1, 0, 1, 1, 2)], # 세로
#         [(1, 1, 0, 1, 0), (1, 1, 1, 0, 1), (1, 1, 1, 1, 2)]] # 대각선

# # visited = set()

# q = deque()
# q.append((0, 0, 0, 1, 0)) # (1, 1), (1, 2) : 파이프의 초기 위치 idx로 변환
# answ = 0
# while q:
#     x1, y1, x2, y2, status = q.popleft()
#     # if (x1, y1, x2, y2) in visited:
#     #     continue
#     # visited.add((x1, y1, x2, y2))
#     if x2 == N-1 and y2 == N-1:
#         answ += 1
#         continue
    
#     for m in move[status]:
#         dx1, dy1, dx2, dy2 = x1+m[0], y1+m[1], x2+m[2], y2+m[3]
#         if dy2 < N and dx2 < N: # 끝에 파이프만 보면 됨
#             if not room[dx2][dy2]:
#                 if m[-1] == 2:
#                     if not room[dx1+1][dy1] and not room[dx2-1][dy2]:
#                         q.append((dx1, dy1, dx2, dy2, m[-1]))
#                 else:
#                     q.append((dx1, dy1, dx2, dy2, m[-1]))
    
# print(answ)

# dfs
import sys
input = sys.stdin.readline

N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
if room[N-1][N-1] == 1:
    print(0)
    quit()
    
answ = 0
def dfs(x, y, position): # 뒤에 파이프의 x와 y만 보면 됨
    global answ
    if x == N-1 and y == N-1:
        answ += 1
        return
    
    if x+1 < N and y+1 < N:
        if not room[x][y+1] and not room[x+1][y] and not room[x+1][y+1]:
            dfs(x+1, y+1, 2) # - => 0, l => 1, \ => 2
        
    if x < N and y+1 < N:
        if position == 0 or position == 2:
            if not room[x][y+1]:
                dfs(x, y+1, 0)
    
    if x+1 < N and y < N:
        if position == 1 or position == 2:
            if not room[x+1][y]:
                dfs(x+1, y, 1)
                
dfs(0, 1, 0)
print(answ)