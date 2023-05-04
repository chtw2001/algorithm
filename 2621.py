maze = []
for _ in range(5):
    c, n = map(str, input().split())
    maze.append((int(n), c))
maze.sort()

num_set = set()
color_set = set()

for n, c in maze:   # duplication check
    num_set.add(n)
    color_set.add(c)

linear = True
num_ex = maze[0][0]
for n, c in maze[1:]:   # linear check
    if num_ex == 9:
        if n != 0:
            linear = False
            break
        num_ex = 0
    else:
        if n - num_ex != 1:
            linear = False
            break
        num_ex = n

if linear and len(color_set) == 1:
    print(maze[-1][0]+900)
    quit()

if len(num_set) == 2:
    first, second = maze[0][0], maze[-1][0]
    first_cnt = 1
    for n, c in maze[1:-1]:
        if first == n:
            first_cnt += 1
        else:
            break
    second_cnt = 5 - first_cnt
    if first_cnt == 4:
        print(maze[0][0] + 800)
    elif second_cnt == 4:
        print(maze[-1][0] + 800)
    elif first_cnt == 3:
        print(maze[0][0]*10 + maze[-1][0]+700)
    elif second_cnt == 3:
        print(maze[-1][0]*10 + maze[0][0]+700)
    quit()

if len(color_set) == 1:
    print(maze[-1][0]+600)
    quit()

if linear == True:
    print(maze[-1][0]+500)
    quit()

if len(num_set) == 3:
    ex = maze[0][0]
    cnt = 0
    for n, c in maze[1:]:
        if ex == n:
            cnt += 1
        else:
            cnt = 0
            ex = n
        if cnt == 2:
            print(ex+400)
            quit()

if len(num_set) == 3:
    ex = maze[0][0]
    cnt, list_ex = 0,[]
    for n, c in maze[1:]:
        if ex == n:
            list_ex.append(ex)
            cnt += 1
            ex = n
        else:
            ex = n
        if cnt == 2:
            print(max(list_ex)*10+min(list_ex)+300)
            quit()

if len(num_set) == 4:
    ex = maze[0][0]
    for n, c in maze[1:]:
        if ex == n:
            print(ex+200)
            quit()
        else:
            ex = n

print(maze[-1][0]+100)