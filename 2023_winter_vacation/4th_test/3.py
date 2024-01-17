import sys
input = sys.stdin.readline

N, M = map(int, input().split())
origin = [input().strip() for _ in range(N)]
check = [input().strip() for _ in range(M)]

union = set()
for string in origin:
    ex = ''
    for alpha in string:
        ex += alpha
        union.add(ex)
        
answ = 0
for string in check:
    if string in union:
        answ += 1
        
print(answ)