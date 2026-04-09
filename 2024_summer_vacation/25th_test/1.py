import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
student = defaultdict(dict)
for _ in range(N):
    S, G = map(int, input().split())
    try:
        student[G][S] += 1
    except:
        student[G][S] = 1

grouped = dict()
ex = 0
for i in range(1, 3):
    for j in range(2):
        try:
            ex += student[i][j]
        except:
            pass
grouped[0] = ex # 1~2 학년 성별 구분 없이

ex = 0
for i in range(3, 5):
    try:
        ex += student[i][1]
    except:
        pass
grouped[1] = ex # 3~4 학년 남자

ex = 0
for i in range(3, 5):
    try:
        ex += student[i][0]
    except:
        pass
grouped[2] = ex # 3~4 학년 야자

ex = 0
for i in range(5, 7):
    try:
        ex += student[i][1]
    except:
        pass
grouped[3] = ex # 5~6 학년 남자

ex = 0
for i in range(5, 7):
    try:
        ex += student[i][0]
    except:
        pass
grouped[4] = ex # 5~6 학년 여자
    

answ = 0
for i in range(5):
    answ += (grouped[i] + K-1) // K

print(answ)