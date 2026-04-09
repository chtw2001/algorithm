import sys
input = sys.stdin.readline

try:
    while True:
        N, B, M = map(float, input().split())
        answ = 0
        curr_money = N
        MOD = B*(0.01)
        while M >= curr_money:
            answ += 1
            curr_money += curr_money*MOD
        
        print(answ)
        
except:
    quit()