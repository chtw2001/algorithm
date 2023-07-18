from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
people = deque(deque() for _ in range(n))
cnt = 1
for i in range(n):
    for _ in range(n):
        people[i].append(cnt)
        cnt += 1

def run():
    dict = defaultdict(int)
    dict['RO'] = (order['RO'] // n)*n
    dict['RE'] = (order['RE'] // n)*n
    dict['CO'] = (order['CO'] // n)*n
    dict['CE'] = (order['CE'] // n)*n
    
    

    i = 0
    while i < len(order_list):
        if dict[order_list[i]]:
            del order_list[i]
            dict[order_list[i]] -= 1
        else:
            i += 1
    if order['RO'] or order['RE']:
        if order['CE'] or order['CO']:
            for list in order_list:
                if list == 'RO':
                    for i in range(0, n, 2):
                        people[i].rotate(1)
                        
                elif list == 'RE':
                    for i in range(1, n, 2):
                        people[i].rotate(1)
                
                elif list == 'CO':
                    for i in range(0, n, 2):
                        ex = deque()
                        for j in range(n):
                            ex.append(people[j][i])     
                        ex.rotate(1)
                        for j in range(n):
                            people[j][i] = ex[j]
                else:
                    for i in range(1, n, 2):
                        ex = deque()
                        for j in range(n):
                            ex.append(people[j][i])
                        ex.rotate(1)
                        for j in range(n):
                            people[j][i] = ex[j]
        else:
            if order['RO']:
                for i in range(0, n, 2):
                    people[i].rotate(order['RO'])
            if order['RE']:
                for i in range(1, n, 2):
                    people[i].rotate(order['RE'])
    else:
        if order['CO']:
            for i in range(0, n, 2):
                ex = deque()
                for j in range(n):
                    ex.append(people[j][i])     
                ex.rotate(order['CO'])
                for j in range(n):
                    people[j][i] = ex[j]
        if order['CE']:
            for i in range(1, n, 2):
                ex = deque()
                for j in range(n):
                    ex.append(people[j][i])
                ex.rotate(order['CE'])
                for j in range(n):
                    people[j][i] = ex[j]
    order['RO'] = 0
    order['RE'] = 0
    order['CO'] = 0
    order['CE'] = 0
        
order = defaultdict(int)
order_list = deque()
for _ in range(q):
    ex = input().strip()
    if ex[0] == 'S':
        ex = list(map(int, ex[1:].split()))
        run()
        order_list = deque()
        people[ex[0]-1][ex[1]-1], people[ex[2]-1][ex[3]-1] = people[ex[2]-1][ex[3]-1] , people[ex[0]-1][ex[1]-1] 
    else:
        order_list.append(ex)
        order[ex] += 1

for i in range(n):
    for j in range(n):
        print(people[i][j], end=' ')
    print()