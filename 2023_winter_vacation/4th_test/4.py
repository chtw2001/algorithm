N = int(input())
ary = list(map(int, input().split()))

visited = [0]*N
parent = -1
answ = dict()
i = 0
while i < N:
    if visited[ary[i]]:
        parent = ary[i]
        i += 1
        continue
    answ[ary[i]] = parent
    parent = ary[i]
    visited[ary[i]] = 1
    i += 1

print(len(answ))
print(*answ.values())