import sys
input = sys.stdin.readline

n, d = map(int, input().split())
d_want = []
for _ in range(d):
    d_want.append(int(input()))

q = [0]*(n+1)

for i in d_want: # 200,000
    ex = i
    while not q[ex]: # 모든 높이를 탐색 (20)
        ex = ex // 2
        if not ex:
            q[i] = 1
            print(0)
            break
    if ex:
        exex = ex
        while ex:   # 모든 높이를 탐색 (20)
            if q[ex]:
                exex = ex
            ex = ex // 2
        print(exex)