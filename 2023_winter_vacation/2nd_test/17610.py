# 4번
K = int(input())
ary = list(map(int, input().split()))
s = sum(ary)+1
available = [0]*(s)

def dfs(left, right, depth):
    if depth == K:
        available[abs(left-right)] = 1
        return

    dfs(left+ary[depth], right, depth+1)
    dfs(left, right+ary[depth], depth+1)
    dfs(left, right, depth+1)
    

dfs(0, 0, 0)

answ = 0
for i in range(1, s):
    if not available[i]:
        answ += 1

print(answ)