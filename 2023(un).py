n = int(input())

# 2,3,5,7,11,13,17,19,23,
maze = pow(10, n+1)
maze[1] = 1
answ = []
r_answ = []
for i in range(2, pow(10, n)):
    if maze[i] == 0:
        if len(str(i)) == n:
            answ.append(i)
        for j in range(2*i, pow(10, n), i):
            maze[j] = 1

if n == 1:
    for i in answ:
        print(i)
else:
    for i in answ:
        ex = 0
        for j in range(1, n):
            if maze[int(str(i)[:j])]:
                break
            ex += 1
        if ex == n-1:
            r_answ.append(i)
    for i in r_answ:
        print(i)
