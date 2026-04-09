n = int(input())

score = []
for i in range(1, n+1):
    score.append(int(input())) # 입력 순서가 레벨, 해당 레벨에서 얻는 점수 input
    
answ = 0
for i in range(n-1, 0, -1):
    if score[i] <= score[i-1]:
        ex = score[i-1] - score[i] + 1
        score[i-1] -= ex
        answ += ex

print(answ)