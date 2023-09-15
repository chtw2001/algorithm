n = int(input())

start = 0
answ = -1
exq = []

while start <= n:
    q = []
    start += 1
    q.append(n)
    q.append(start)
    second = start
    ex = n - start

    while ex >= 0:
        q.append(ex)
        ex2 = ex
        ex = second - ex
        second = ex2
    if answ > len(q):
        print(len(exq))
        for i in exq:
            print(i, end=' ')
        quit()
    else:
        answ = len(q)
        exq = q