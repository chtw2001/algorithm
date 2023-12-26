n = int(input())
tower = list(map(int, input().split()))

answ = 0
i = 0
def check():
    global answ, i
    try:
        if tower[i] > tower[i+1]:
            i += 1
            check()
        else:
            return
    except:
        return 

while i < n:
    try:
        if tower[i] > tower[i+1]:
            answ += 1
            i += 1
            check()
            i += 1
        else:
            answ += 1
            i += 1
    except:
        answ += 1
        break
        
print(answ)