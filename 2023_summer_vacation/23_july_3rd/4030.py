import sys
input = sys.stdin.readline

sqrt = set()
can = []
for i in range(2, pow(10, 5)):
    sqrt.add(i**2)
    if i*(i+1)//2 + 1 in sqrt:
        can.append(i*(i+1)//2 + 1)

case_cnt = 1
while True:
    answ = 0
    
    s, e = map(int, input().split())
    if s == 0 and e == 0:
        quit()
    
    for target in can:
        start = s + 1
        end = e - 1
        while start <= end:
            mid = (start + end) // 2
            if target < mid:
                end = mid - 1
            elif target > mid:
                start = mid + 1
            else:
                answ += 1
                break

    print(f'Case {case_cnt}: {answ}')
    case_cnt += 1