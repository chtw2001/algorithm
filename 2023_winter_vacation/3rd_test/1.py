b_year, b_month, b_day = map(int, input().split())
set_year, set_month, set_day = map(int, input().split())

age = set_year - b_year
if set_month > b_month:
    print(age)
elif set_month == b_month:
    if set_day >= b_day:
        print(age)
    else:
        print(max(age-1, 0))
else:
    print(max(age-1, 0))

print(age+1)

if not age:
    print(0)
else:
    print(age)