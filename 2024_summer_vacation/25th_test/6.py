W, H = map(int, input().split())

def check(x, y, flag, direction):
    if x == W and y == H:
        return 1
    
    answ = 0
    if flag == 0:
        dx, dy = x+1, y
        if dx <= W and dy <= H:
            if direction: # 이전에 북쪽으로 향하고 있다면
                answ += check(dx, dy, 0, 1) % 100000
            else:
                answ += check(dx, dy, 1, 1) % 100000
        
        dx, dy = x, y+1
        if dx <= W and dy <= H:
            if direction: # 이전에 북쪽으로 향하고 있다면
                answ += check(dx, dy, 1, 0) % 100000
            else:
                answ += check(dx, dy, 0, 0) % 100000
                
    else: # 방향을 이전에 바꾼 경우
        if direction:   # 이전에 북쪽으로 향하고 있다면
            dx, dy = x+1, y # 북쪽으로만 가야함
            if dx <= W and dy <= H:
                answ += check(dx, dy, 0, 1) % 100000
        else:
            dx, dy = x, y+1 # 동쪽으로만 가야함
            if dx <= W and dy <= H:
                answ += check(dx, dy, 0, 0) % 100000
    
    return answ % 100000

print((check(2, 1, 0, 1) + check(1, 2, 0, 0)) % 100000)
