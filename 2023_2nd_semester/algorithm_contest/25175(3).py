n, m, k = map(int, input().split())

move = 0
if k < 3:
    move = 3 - k
    while move != 0:
        m -= 1
        if m == 0:
            m = n
        move -= 1
elif k > 3:
    move = k - 3
    while move != 0:
        m += 1
        if m == n+1:
            m = 1
        move -= 1
        
print(m)