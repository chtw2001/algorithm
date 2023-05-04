import sys
input = sys.stdin.readline
# 뒤뒤뒤, 뒤뒤앞, 뒤앞뒤, 뒤앞앞, 앞뒤뒤, 앞뒤앞, 앞앞뒤, 앞앞앞 
dic = {}
dic['TTT'] = 0
dic['TTH'] = 1
dic['THT'] = 2
dic['THH'] = 3
dic['HTT'] = 4
dic['HTH'] = 5
dic['HHT'] = 6
dic['HHH'] = 7
answ = [0]*8

def check(ex, str_idx, str): # len(ex)가 3개가 되면 딕셔너리 탐색해서 answ 배열에 넣기
    if str_idx == 39 and len(ex) < 3:
        return
    if len(ex) == 3:         # str에서 out of range나지 않게 해야함
        answ[dic[ex]] += 1
        return
    check(ex+str[str_idx+1], str_idx+1, str) 

n = int(input()) 
for _ in range(n):
    ex = input().strip()
    for i in range(len(ex)):
        check(ex[i], i, ex)
    for i in answ:
        print(i, end=' ')
    print()
    answ = [0]*8