import datetime
N = int(input())
start_date = datetime.date(2014,4,2)
answ_date = start_date + datetime.timedelta(days=N-1)
print(answ_date)
