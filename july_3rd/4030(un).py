import sys
input = sys.stdin.readline

sqrt = set()
tri = set()
for i in range(1, pow(10, 5)):
    sqrt.add(i**2)
    tri.add(i*(i+1)//2)

case_cnt = 1
while True:
    
    answ = 0
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    for i in range(a+1, b):
        if i in sqrt and i - 1 in tri:
            answ += 1
    
    print(f'Case {case_cnt}: {answ}')
    case_cnt += 1