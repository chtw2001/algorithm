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
            if dict[i] >= 3:
                answ += i*(dict[i]//2)
            ex = i
            continue
        even += 1
        answ += i*(dict[i]//2)

if odd:
    new = ''
    new += answ
    new += ex
    new += answ[::-1]
    print(new)
else:
    answ += answ[::-1]
    print(answ)