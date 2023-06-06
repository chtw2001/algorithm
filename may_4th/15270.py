import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    maze[a].append(b)
    maze[b].append(a)

answ = -sys.maxsize
def check(num, union):
    global answ
    if num == n:
        answ = max(answ, len(union))
        return
    if num not in union:
        check(num+1, union)
        union.add(num)
        for i in maze[num]:
            if i not in union:
                union.add(i)
                check(num+1, union)
                union.discard(i)
        union.discard(num)
    else:
        check(num+1, union)

check(1, set())

if not m:
    print(1)
else:
    if answ == n:
        print(n)
    elif answ % 2:
        print(answ)
    else:
        print(answ + 1)