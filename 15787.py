from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [deque([0]*20) for _ in range(n)]
order = [list(map(int, input().split())) for _ in range(m)]

for ord in order:
    if ord[0] == 1:
        train[ord[1]-1][ord[2]-1] = 1
    elif ord[0] == 2:
        train[ord[1]-1][ord[2]-1] = 0
    elif ord[0] == 3:
        train[ord[1]-1].rotate(1)
        train[ord[1]-1][0] = 0
    else:
        train[ord[1]-1].rotate(-1)
        train[ord[1]-1][-1] = 0

def check(arr):
    ex = 0
    for i in range(20):
        ex += pow(2, i)*arr[i] # 기차 1개의 좌석 배치 
        # 2^0 ~ 2^19
    return ex

duplicate = set()
dupli = 0
for i in train:
    ex = check(i)
    if ex in duplicate:
        dupli += 1
    else:
        duplicate.add(ex)

print(n - dupli)