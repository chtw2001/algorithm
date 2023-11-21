N = int(input())
ary = list(map(int, input().split()))
ary.insert(0, 0)
visited = [0]*(N+1)
answ = 0
idx = int(input())
def check(idx):
    global answ
    if idx <= 0 or idx > N or visited[idx]:
        return
    visited[idx] = 1
    answ += 1
    check(idx + ary[idx])
    check(idx - ary[idx])
    
    return

check(idx)
print(answ)