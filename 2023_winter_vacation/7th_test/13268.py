# 1번 셔틀런
N = int(input())

ary = [0, 1, 0, 1, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1]
length = 20

idx = 0
while N:
    if N - 5 > 0:
        N -= 5
        idx += 1
    else:
        if ary[idx%length] < ary[(idx+1)%length]: # forward
            print(ary[(idx+1)%length])
        else:                                     # backward
            if not N - 5:
                print(ary[(idx+1)%length])
            else:
                print(ary[idx%length])
        quit()