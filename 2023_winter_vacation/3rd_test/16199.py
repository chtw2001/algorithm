# 1번
b_year, b_month, b_day = map(int, input().split())
set_year, set_month, set_day = map(int, input().split())

age = set_year - b_year
if set_month > b_month: # 생일 지남
    print(age)
elif set_month == b_month: 
    if set_day >= b_day: # 생일 지남
        print(age)
    else:
        print(max(age-1, 0)) # 생일 안지남
else:
    print(max(age-1, 0)) # 생일 안지남

print(age+1)

if not age:
    print(0)
else:
    print(age)