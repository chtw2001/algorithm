# 4번 로마 숫자
ary = [input().rstrip() for _ in range(2)]
dict = dict()
dict['I'] = 1
dict['V'] = 5
dict['X'] = 10
dict['L'] = 50
dict['C'] = 100
dict['D'] = 500
dict['M'] = 1000
dict['IV'] = 4
dict['IX'] = 9
dict['XL'] = 40
dict['XC'] = 90
dict['CD'] = 400
dict['CM'] = 900

dp = ['']*4001

dp[1] = 'I'
dp[5] = 'V' 
dp[10] = 'X' 
dp[50] = 'L'
dp[100] = 'C'
dp[500] = 'D'
dp[1000] = 'M'

dp[4] = 'IV' # dp[5] - dp[1]
dp[9] = 'IX' # dp[10] - dp[1]
dp[40] = 'XL'
dp[90] = 'XC'
dp[400] = 'CD'
dp[900] = 'CM'

num = 0
for string in ary:
    try:
        num += dict[string]
    except:
        i = 0
        list_ = [0]*len(string)
        while i < len(string)-1:
            if dict[string[i]] < dict[string[i+1]]:
                num += dict[string[i]+string[i+1]]
                list_[i], list_[i+1] = 1, 1
                i += 2
            else:
                num += dict[string[i]]
                list_[i] = 1
                i += 1
        if list_[-1]:
            continue
        num += dict[string[-1]]

fixed = [1, 5, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
base = 0
for i in range(2, num+1):
    if dp[i]:
        if i not in [4, 9]:
            base += 1
        continue
    
    dp[i] += dp[fixed[base]] + dp[i-fixed[base]]

print(num)
print(dp[num])
