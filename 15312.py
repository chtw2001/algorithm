move = (3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1)

dic = dict()
for i in range(26):
    dic[chr(i+65)] = move[i]

n = input()
m = input()
length = len(n)

maze = [0]*(length*2-1)
j = 0
for i in range(length-1):
    maze[j] = dic[n[i]] + dic[m[i]]
    j += 1
    maze[j] = dic[m[i]] + dic[n[i+1]]
    j += 1

maze[-1] = dic[n[-1]] + dic[m[-1]]

length = length*2 - 1
while True:
    length -= 1
    if length == 1:
        break
    for i in range(length):
        maze[i] = (maze[i] + maze[i+1]) % 10

print(str(maze[0]) + str(maze[1]))