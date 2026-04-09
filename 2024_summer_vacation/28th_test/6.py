import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ary = [[0]*(N+1) for _ in range(M+1)]
for i in range(M):
    ex = list(map(int, input().split()))
    for ele in ex[1:]:
        ary[i+1][ele] += 1


def subset(element, length):
    def back_track(start, path):
        if path:
            subsets.append(path[:])
        for i in range(start, length):
            path.append(element[i])
            back_track(i+1, path)
            path.pop()

    subsets = []
    back_track(0, [])
    return subsets

subsets = subset([i+1 for i in range(M)], M)

answ = 11
for subset_ in subsets:
    ex = [0]*(N+1)
    for i in subset_:
        for j in range(1, N+1):
            ex[j] += ary[i][j]
    
    flag = 0
    for i in ex[1:]:
        if not i:
            flag = 1
            break
    if not flag:
        answ = min(answ, len(subset_))
    
    
if answ != 11:
    print(answ)
else:
    print(-1)
