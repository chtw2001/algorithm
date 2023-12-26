import sys
input = sys.stdin.readline

N = int(input())
medi = {}
for _ in range(N):
    works, medicine = map(int, input().split())
    medi[works] = medicine

R = int(input())
for _ in range(R):
    ex = list(map(int, input().split()))
    answ = []
    sick = ex[0]
    for key in ex[1:]:
        try:
            if medi[key]:
                pass
            else:
                pass
            sick -= 1 
            answ.append(medi[key])
        except:
            print("YOU DIED")
            break
    if not sick:
        for i in answ:
            print(i, end=' ')
        print()
    