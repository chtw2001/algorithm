import sys
input = sys.stdin.readline

_, l = map(int, input().split())
N = int(input())

store = []
for i in range(N):
    store.append(list(map(int, input().split())))

p, v = map(int, input().split()) # position, value

answ = 0
for _p, _v in store:
    if (p, _p) in {(3, 1), (1, 3)}:
        answ += _v + v
    elif (p, _p) in {(4, 2), (2, 4)}:
        if p == 2:
            answ += _ - v + l - _v
        else:
            answ += l - v + _ - _v
    elif (p, _p) in {(2, 3), (3, 2)}:
        if p == 2:
            answ += v + l - _v
        else:
            answ += l - v + _v
    elif (p, _p) in {(1, 4), (4, 1)}:
        if p == 4:
            answ += v + _ - _v
        else:
            answ += _ - v + _v
    elif (p, _p) in {(1, 2), (2, 1)}:
        answ += min(v + _v + l, _ - v + _ - _v + l)
    elif (p, _p) in {(3, 4), (4, 3)}:
        answ += min(v + _v + _, _ - v + _ - _v + _)
    else:
        answ += abs(v - _v)

print(answ)