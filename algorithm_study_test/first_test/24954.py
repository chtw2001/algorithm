import sys
input = sys.stdin.readline

N = int(input())
potion = list(map(int, input().split()))

sale_info = [[] for _ in range(N)]
for i in range(N):
    num = int(input())
    _dict = dict()
    for _ in range(num):
        p, n = map(int, input().split())
        _dict[p-1] = n
        
    sale_info[i] = _dict

answ = sys.maxsize
def cal_cost(_list, p): # 이미 구매한 물약, 현재 구매할 물약 번호
    ex = 0
    for i in _list:
        try:
            ex += sale_info[i][p]
        except:
            pass
    
    return max(1, potion[p] - ex)
    

def check(_list, cost, depth): # 이미 구매한 물약, 비용, 재귀 층
    global answ
    if cost > answ:
        return
    if depth == N-1:
        answ = min(answ, cost)
        return
    for i in range(N):
        if i in _list:
            continue
        _list.add(i)
        ex = cal_cost(_list, i)
        check(_list, cost + ex, depth+1)
        _list.discard(i)

for i in range(N):
    check({i}, potion[i], 0)

print(answ)