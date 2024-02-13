# 3번 자바의 형변환
import sys
input = sys.stdin.readline

N = int(input())
tree = dict()
while N-1:
    child, parent = map(str, input().split())
    tree[child] = parent

    N -= 1
    
A, B = map(str, input().split())
check = A
flag = 0
while True:
    try:
        if tree[check] == B:
            print(1)
            flag = 1
            break
        else:
            check = tree[check]
    except KeyError:
        break
if flag:
    quit()

check = B
while True:
    try:
        if tree[check] == A:
            print(1)
            flag = 1
            break
        else:
            check = tree[check]
    except KeyError:
        break
    
if flag:
    quit()
else:
    print(0)