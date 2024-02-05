# 3번 현대모비스 소프트웨어 아카데미

N, M = map(int, input().split())
list_ = list(map(int, input().split()))
list_.sort() # O(N*logN) n => 10^5

s, e = 0, N-1
answ = 0
while s < e: # O(N)
    if list_[s] + list_[e] >= M:
        answ += 1
        s += 1
        e -= 1
    else:
        s += 1

print(answ)