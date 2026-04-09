# 2번 서강근육맨
import sys
input = sys.stdin.readline
N = int(input())
ary = sorted(list(map(int, input().split())))

if N == 1:
    print(ary[0])
    quit()

if N % 2:
    answ = ary[-1]
    for i in range(N//2):
        answ = max(answ, ary[i]+ary[-i-2])
else:
    answ = -sys.maxsize
    for i in range(N//2):
        answ = max(answ, ary[i]+ary[-i-1])
    
print(answ)
