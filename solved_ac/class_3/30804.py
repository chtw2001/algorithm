# 과일 탕후루
import sys
input = sys.stdin.readline
N = int(input())
ary = list(map(int, input().split()))
sys.setrecursionlimit(2000001)
fruits = [0]*10

def check(start, end, cnt, answ):
    if end == N:
        return answ
    
    if not fruits[ary[end]]:
        cnt += 1
        
    fruits[ary[end]] += 1
    if cnt > 2:
        fruits[ary[start]] -= 1
        if not fruits[ary[start]]:
            cnt -= 1
        start += 1

    answ = max(answ, end-start+1)
    return check(start, end+1, cnt, answ)

print(check(0, 0, 0, 0))
