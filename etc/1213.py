# 홀수는 1개까지 가능, 짝수는 많아도 상관없음. 
n = input()
dict = {}
for i in range(26):
    dict[chr(65 + i)] = 0

for i in n:
    dict[i] += 1

odd = 0
even = 0
answ = ''
ex = 0
for i in dict.keys():
    if dict[i]:
        if dict[i] % 2:
            if odd:
                print("I'm Sorry Hansoo")
                quit()
            odd += 1
            if dict[i] >= 3:            # 홀수가 있으면 추가
                answ += i*(dict[i]//2)
            ex = i
            continue
        even += 1
        answ += i*(dict[i]//2)

if odd: # 홀수가 있으면
    new = ''
    new += answ
    new += ex           # 가운데에 홀수 알파벳 추가
    new += answ[::-1]
    print(new)
else:
    answ += answ[::-1]
    print(answ)