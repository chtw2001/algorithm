import sys
inpyt = sys.stdin.readline

n, m = map(int, input().split())
maze = sorted(list(map(int, input().split())))

def check(set, str_set, degree, string):
    if degree == m:
        if string not in str_set:
            str_set.add(string)
            print(string[1:])
        return
    for i in range(n):
        if i not in set:
            set.add(i)
            check(set, str_set, degree+1, string+' '+str(maze[i]))
            set.discard(i)

check(set(), set(), 0, '')