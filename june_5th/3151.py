import math
n = int(input())
ary = [0]*(20001)

ex = list(map(int, input().split()))
for i in ex:
    ary[i+10000] += 1

answ = 0
for i in range(20001):
    if ary[i]:
        for j in range(i, 20001):
            if ary[j]:
                k = 10000-i + 10000-j + 10000
                if k < 0 or k > 20000 or k < i or k < j:
                    continue
                if ary[k]:
                    if i == j:
                        if ary[i] >= 2:
                            if j == k:
                                if ary[i] >= 3:
                                    answ += math.factorial(ary[k])/max(1, math.factorial(ary[k]-3))/math.factorial(3)
                                else:
                                    continue
                            else:
                                answ += ary[k]*math.factorial(ary[i])/max(1, math.factorial(ary[i]-2))/math.factorial(2)
                        else:
                            continue
                    elif j == k:
                        if ary[j] >= 2:
                            answ += ary[i]*math.factorial(ary[k])/max(1, math.factorial(ary[k]-2))/math.factorial(2)
                        else:
                            continue
                    elif i == k:
                        if ary[i] >= 2:
                            answ += ary[j]*math.factorial(ary[k])/max(1, math.factorial(ary[k]-2))/math.factorial(2)
                        else:
                            continue
                    else:
                        answ += ary[i]*ary[j]*ary[k]

print(int(answ))