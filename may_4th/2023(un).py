n = int(input())

maze = [False]*pow(10,4)
maze[1] = True
same_length = []
ex = []
prime = []
r_answ = []

for i in range(2, max(pow(10, n)//pow(10,4), 1)):
    if not maze[i]:
        prime.append(i)
        for j in range(2*i, pow(10, 4), i):
            maze[j] = True

if n == 1:
    for i in same_length:
        print(i)
        
elif n < 5:
    for i in same_length:
        ex = 0
        for j in range(1, n):
            if maze[int(str(i)[:j])]:
                break
            ex += 1
        if ex == n-1:
            r_answ.append(i)
    for i in r_answ:
        print(i)
        
else:
    