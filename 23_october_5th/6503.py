from collections import defaultdict
def check(cnt, string, n):
    left, var = 0, 0
    length = len(string)
    answ = [0]*(length+1)
    dict = defaultdict(int)
    
    for i in range(length):
        if dict[string[i]]:
            dict[string[i]] += 1
            cnt += 1
        else:
            dict[string[i]] += 1
            if var == n: # 집합에 없음, 변수 추가 불가능
                while True:
                    dict[string[left]] -= 1
                    cnt -= 1
                    if dict[string[left]]:
                        left += 1
                    else:
                        left += 1
                        cnt += 1
                        break

            else: # 집합에 없음, 변수 추가 가능
                var += 1
                cnt += 1
                
        answ[left] = cnt
        
    return print(max(answ))


while True:
    M = int(input())
    if not M:
        break

    string = list(input())
    check(0, string, M)