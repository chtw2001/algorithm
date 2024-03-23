# 3번 시간표 짜기
import sys
input = sys.stdin.readline

N = int(input())
schedule_num = []
schedule = []
for i in range(N):
    ex = list(map(int, input().split()))
    schedule_num.append(ex[0])
    schedule.append(sorted(ex[1:]))
    
M = int(input())
student = []
student_num = []
for i in range(M):
    ex = list(map(int, input().split()))
    student_num.append(ex[0])
    student.append(sorted(ex[1:]))
    

for i in range(M):
    answ = 0
    for j in range(N):
        ex = 0
        for k in range(schedule_num[j]):
            s, e = 0, student_num[i]-1
            target = schedule[j][k]
            while s <= e:
                mid = (s + e) // 2
                if student[i][mid] < target:
                    s = mid + 1
                elif target < student[i][mid]:
                    e = mid - 1
                else:
                    ex += 1
                    break
        if ex == schedule_num[j]:
            answ += 1
    print(answ)
