import sys
input = sys.stdin.readline

N = int(input())
cp = [list(map(int, input().split())) for _ in range(N)]

def manhattan(p1, p2):
    x = abs(p1[0] - p2[0])
    y = abs(p1[1] - p2[1])
    return x + y

jump = 0
num = 0
point = set()
for i in range(N-2):
    one_two = manhattan(cp[i], cp[i+1])
    two_three = manhattan(cp[i+1], cp[i+2])
    one_three = manhattan(cp[i], cp[i+2])
    ex = one_two + two_three - one_three
    
    if jump < ex:
        jump = ex
        num = one_three
        point = {i, i+1}

answ = num
for i in range(N-1):
    if i in point:
        continue
    answ += manhattan(cp[i], cp[i+1])
    

print(answ)