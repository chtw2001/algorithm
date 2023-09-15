import sys
input = sys.stdin.readline

n = int(input())
a = [0, 0]
b = [0, 0]
ex = 0

def check_a(before, after):
    global a
    if before == 0:
        return
    hour, minute = map(int, after.split(':'))
    b_hour, b_minute = map(int, before.split(':'))
    if minute - b_minute < 0:
        a[1] += (hour - b_hour - 1)*60 + (60 + minute - b_minute)
    else:
        a[1] += (hour - b_hour)*60 + (minute - b_minute)
        
def check_b(before, after):
    global b
    if before == 0:
        return
    hour, minute = map(int, after.split(':'))
    b_hour, b_minute = map(int, before.split(':'))
    if minute - b_minute < 0:
        b[1] += (hour - b_hour - 1)*60 + (60 + minute - b_minute)
    else:
        b[1] += (hour - b_hour)*60 + (minute - b_minute)


for _ in range(n):
    vic, time = map(str, input().split())
    if vic == '1':
        a[0] += 1
    else:
        b[0] += 1
    if a[0] > b[0]:
        check_a(ex, time)
        ex = time
    elif a[0] < b[0]:
        check_b(ex, time)
        ex = time
    else:
        if vic == '1':
            check_b(ex, time)
        else:
            check_a(ex, time)
        ex = 0
    # 비기는 시간이 ex에 들어감

if time != '48:00':
    ex = time
    if a[0] > b[0]:
        check_a(ex, '48:00')
    elif a[0] < b[0]:
        check_b(ex, '48:00')

if len(str(a[1]//60)) == 1:
    print('0' + str(a[1]//60) + ':', end='')
else:
    print(str(a[1]//60)+':', end='')
    
if len(str(a[1]%60)) == 1:
    print('0' + str(a[1]%60))
else:
    print(a[1]%60)
    
if len(str(b[1]//60)) == 1:
    print('0' + str(b[1]//60) + ':', end='')
else:
    print(str(b[1]//60) + ':', end='')
    
if len(str(b[1]%60)) == 1:
    print('0' + str(b[1]%60))
else:
    print(b[1]%60)