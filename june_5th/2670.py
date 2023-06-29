n = int(input())
ary = []

for _ in range(n):
    ary.append(float(input()))
    
dp = [ary[0]]
answ = ary[0]
for i in range(1, n):
    for j in range(i):
        dp[j] *= ary[i]
        answ = max(answ, dp[j], ary[i])
    dp.append(ary[i])

print('%.3f' % answ)