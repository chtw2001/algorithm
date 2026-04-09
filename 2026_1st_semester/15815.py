from collections import deque
string = input()
q = deque()

for i in range(len(string)):
    if string[i].isdigit():
        q.append(int(string[i]))
    else:
        a = q.pop()
        b = q.pop()
        if string[i] == '+':
            q.append(b+a)
        elif string[i] == '-':
            q.append(b-a)
        elif string[i] == '*':
            q.append(b*a)
        elif string[i] == '/':
            q.append(b/a)

print(int(q.pop()))