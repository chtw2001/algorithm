import sys
input = sys.stdin.readline

maze = []
while True:
    ex = input().strip()
    if ex == '*':
        break
    maze.append(ex)
    
def check(string, union, n):
    for i in range(len(string)-n):
        ex = string[i] + string[i+n]
        if ex in union:
            return 0
        else:
            union.add(ex)
    return union

for i in maze:
    if len(i) <= 2:
        print(f'{i} is surprising.')
        continue
    for j in range(1, len(i)):
        union = set()
        ex = check(i, union, j)
        if not ex:
            print(f'{i} is NOT surprising.')
            break
    if ex:
        print(f'{i} is surprising.')