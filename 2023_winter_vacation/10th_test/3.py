import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ary = [int(input()) for _ in range(M)]

def check(mid):
    ex = 0 # 질투심이 최대 mid가 되기 위해 필요한 사람 수
    for i in ary:
        ex += (i + mid-1) // mid
    
    return ex

# 질투심 키우면 필요한 사람수 줄고
# 질투심 낮추면 필요한 사람수 많아짐
s, e = 1, max(ary)
answ = sys.maxsize
while s <= e:
    mid = (s + e) // 2
    target = check(mid)
    
    if target > N:
        s = mid + 1
    else:
        e = mid - 1
        answ = min(answ, mid)      
    
print(answ)
