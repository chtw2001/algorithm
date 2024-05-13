# 1번 호텔 방 번호
while True:
    try:
        N, M = map(int, input().split())
        answ = 0
        for i in range(N, M+1):
            length = 0
            ex = set()
            while i > 0:
                ex2 = i % 10
                ex.add(ex2)
                i -= ex2
                i //= 10
                length += 1
            if length == len(ex):
                answ += 1
        
        print(answ)
    except:
        quit()
