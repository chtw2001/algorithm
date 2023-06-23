import sys
input = sys.stdin.readline

n, d = map(int, input().split())
d_want = []
for _ in range(d):
    d_want.append(int(input()))

q = [0]*(n+1)

for i in d_want:
    ex = i
    while not q[ex]:
        ex = ex // 2
        if not ex:
            q[i] = 1
            print(0)
            break
    if ex:
        exex = ex
        while ex:
            if q[ex]:
                exex = ex
            ex = ex // 2
        print(exex)