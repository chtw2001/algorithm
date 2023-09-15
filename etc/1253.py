n = int(input())
maze = list(map(int, input().split()))
maze.sort()
dic = {}

for i in range(len(maze)):      # 가능한 조합을 모두 딕셔너리에 삽입
    for j in range(i+1, len(maze)):
        dic[maze[i]+maze[j]] = 1

# for i in range(len(maze)-1):    # 중복된 수도 있을 수 있음 
#     if maze[i] == maze[i+1]:    # "두" 수의 합이므로 주석처리함
#         dic[maze[i]] = 1

answ = 0
for i in maze[2:]:              # 첫번째, 두번째 요소는 정답이 될 수 없음
    try:
        if dic[i]:
            answ += 1
    except:
        continue

print(answ)