import sys
input = sys.stdin.readline

info_dict = dict()
N, L = map(int, input().split())
for _ in range(N):
    D, R, G = map(int, input().split())
    info_dict[D] = [R, G]

answ = 0
for i in range(1, L+1):
    answ += 1
    try:
        if info_dict[i]:
            ex = answ
            R, G = info_dict[i][0], info_dict[i][1]
            if ex // (R + G):
                ex %= (R + G)
                if ex // R:
                    pass
                else:
                    answ += R - ex
            else:
                if ex // R:
                    pass
                else:
                    answ += R - ex
    except:
        pass

print(answ)