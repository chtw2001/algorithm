# 2번 간판
import sys
input = sys.stdin.readline
N = int(input())
name = input().rstrip()
name_length = len(name)
ary = [input().rstrip() for _ in range(N)]

answ = 0

for element in ary:
    length = len(element)
    flag = 0
    for idx in range(length): # str index
        ex_idx = idx

        for i in range(1, length): # slicing unit
            ex = ''
            while name_length != len(ex) and ex_idx < length:
                ex += element[ex_idx]
                ex_idx += i

            if ex == name:
                answ += 1
                flag = 1
                break
            else:
                ex_idx = idx
        if flag:
            break

print(answ)
