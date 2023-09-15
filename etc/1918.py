from collections import defaultdict
maze = list(map(str, input()))
q = []
dic = defaultdict(list)

dic['+'] = 2
dic['-'] = 2
dic['*'] = 3
dic['/'] = 3
dic['('] = 1
dic[')'] = 10

for i in maze:
    ex = len(q)
    if not dic[i]:
        print(i, end='')
    else:
        if not ex:
            q.append(i)
        elif i == '(':
            q.append(i)
        elif i == ')':
            while q[ex-1] != '(':
                print(q.pop(), end='')
                ex -= 1
            q.pop()
        elif dic[q[ex-1]] >= dic[i]:
            while dic[q[ex-1]] in (2, 3) and dic[q[ex-1]] >= dic[i]:
                print(q.pop(), end='')
                ex -= 1
                if ex < 1:
                    break
            q.append(i)
        elif dic[q[ex-1]] < dic[i]:
            q.append(i)
        
while q:
    print(q.pop(), end='')