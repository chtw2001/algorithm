# 사전 순 최대 공통 부분 수열
N = int(input())
ary1 = list(map(int, input().split()))
ary1_ = ary1.copy()
M = int(input())
ary2 = list(map(int, input().split()))
ary2_ = ary2.copy()

answ = []
    
while ary1 and ary2:
    ary1_max = max(ary1)
    if ary1_max in ary2:
        answ.append(ary1_max)
        if ary1.index(ary1_max)+1 == N or ary2.index(ary1_max)+1 == M:
            break

        ary1 = ary1[ary1.index(ary1_max)+1:]
        ary2 = ary2[ary2.index(ary1_max)+1:]
    else:
        if ary1.index(ary1_max)+1 == N:
            break
        ary1.pop(ary1.index(ary1_max))
        N -= 1

answ2 = []
while ary1_ and ary2_:
    ary2_max = max(ary2_)
    if ary2_max in ary1_:
        answ2.append(ary2_max)
        if ary2_.index(ary2_max)+1 == M or ary1_.index(ary2_max)+1 == N:
            break

        ary2_ = ary2_[ary2_.index(ary2_max)+1:]
        ary1_ = ary1_[ary1_.index(ary2_max)+1:]
    else:
        if ary2_.index(ary2_max)+1 == N:
            break
        ary2_.pop(ary2_.index(ary2_max))
        M -= 1

if answ or answ2:
    if len(answ2) > len(answ):
        print(len(answ2))
        print(*answ2)
    else:
        print(len(answ))
        print(*answ)
else:
    print(0)
